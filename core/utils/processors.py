# -*- coding: utf-8 -*-
#
# watermark processors for django-imagekit
# some inspiration from http://code.activestate.com/recipes/362879-watermark-with-pil/
#
import weakref

from imagekit.lib import Image
from imagekit.lib import ImageEnhance
from imagekit.processors.resize import ResizeToFit


def _process_coords(img_size, wm_size, coord_spec):
    """
    Given the dimensions of the image and the watermark as (x,y) tuples and a
    location specification, return the coordinates where the watermark should
    be placed according to the specification in a (x,y) tuple.

    Specification can use pixels, percentage (provided as a string, such as
    "30%"), or keywords such as top, bottom, center, left and right.
    """
    (sh, sv) = coord_spec
    if sh in ('top','bottom') or sv in ('left','right'):
        # coords were written in wrong order, but there's an easy fix
        (sv, sh) = coord_spec

    if isinstance(sh, basestring) and '%' in sh:
        sh = int(img_size[0] * float(sh.rstrip("%")) / 100)

    if isinstance(sh, int) and sh < 0:
        sh = img_size[0] - wm_size[0] + sh

    if sh == 'left':
        sh = 0
    elif sh == 'center':
        sh = (img_size[0] - wm_size[0]) / 2
    elif sh == 'right':
        sh = img_size[0] - wm_size[0]


    if isinstance(sv, basestring) and '%' in sv:
        sv = int(img_size[1] * float(sv.rstrip("%")) / 100)

    if isinstance(sv, int) and sv < 0:
        sv = img_size[1] - wm_size[1] + sv

    if sv == 'top':
        sv = 0
    elif sv == 'center':
        sv = (img_size[1] - wm_size[1]) / 2
    elif sv == 'bottom':
        sv = img_size[1] - wm_size[1]

    return (sh, sv)


class Watermark(object):
    """
    Creates a watermark using an image.

    ``watermark`` is the path to the image to be overlaid on the processed
    image, or a storage (File-like) object that allows accessing the image.
    """

    def get_watermark(self):
        # open the image despite the format that the user provided for it
        if self.watermark:
            return self.watermark
        if self.watermark_image:
            return self.watermark_image

        if self.watermark_file:
            return Image.open(self.watermark_file)
        if self.watermark_path:
            return Image.open(self.watermark_path)

    def _get_watermark(self):
        if not self.cache_mark:
            return self.get_watermark()
        else:
            # cache watermark and use it
            if self.cache_get_wm is None:
                wm = None
            else:
                wm = self.cache_get_wm()

            if wm is None:
                wm = self.get_watermark()
                self.cache_get_wm = weakref.ref(wm)
                return wm


    def _fill_options(self, opacity=1.0, position=('center','center'),
                      repeat=False, scale=None, cache_mark=True):
        """
            Some properties that are used in processors based on this class are:

            ``opacity`` may be specified as a float ranging from 0.0 to 1.0.

            ``position`` is a tuple containing coordinates for horizontal and
            vertical axis. Instead of coordinates you may use strings such as "left",
            "center", "right", "top" or "bottom". You may also specify percentage
            values such as "70%". Negative values will count from the opposite
            margin. As such, `('66%', 'bottom')` and `('-33%', 'bottom')` are
            equivalent.

            ``scale`` can be a numeric scale factor or ``True``, in which case the
            watermark will be scaled to fit the base image, using the mechanics from
            ``ResizeToFit``.

            ``repeat`` specifies if the watermark should be repeated throughout the
            base image. The repeat pattern will be influenced by both ``scale`` and
            ``position``.

            ``cache_mark`` specifies if the watermark layer that is merged into the
            images should be cached rather than calculated every time a processing
            runs, allowing a trade of CPU time for memory usage.
        """

        self.opacity = opacity
        self.position = position
        self.repeat = repeat
        self.scale = scale
        self.cache_mark = cache_mark
        if cache_mark:
            self.cache_get_wm = None

    def process(self, img):

        # get watermark
        wm = self._get_watermark()
        wm_size = wm.size

        if self.scale:
            if isinstance(self.scale, (int, float)) and self.scale != 1:
                wm_size[0] *= self.scale
                wm_size[1] *= self.scale
                wm = wm.scale(wm_size)
            elif self.scale == True:
                wm = ResizeToFit(width=img.size[0], height=img.size[1],
                    upscale=True).process(wm)
                wm_size = wm.size


        # prepare image for overlaying (ensure alpha channel)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        # create a layer to place the watermark
        layer = Image.new('RGBA', img.size, (0,0,0,0))
        coords = _process_coords(img.size, wm_size, self.position)

        if self.repeat:
            sx = coords[0] % wm_size[0] - wm_size[0]
            sy = coords[1] % wm_size[1] - wm_size[1]
            for x in range(sx, img.size[0], wm_size[0]):
                for y in range(sy, img.size[1], wm_size[1]):
                    layer.paste(wm, (x,y))
        else:
            layer.paste(wm, coords)


        if self.opacity < 1:
            alpha = layer.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(self.opacity)
            layer.putalpha(alpha)

        # merge watermark layer
        img = Image.composite(layer, img, layer)

        return img

    def __init__(self, watermark, **kwargs):
        # fill in base defaults
        defaults = dict(opacity=1.0)
        defaults.update(kwargs)
        self._fill_options(**defaults)

        # fill in specific settings
        self.watermark = None
        self.watermark_image = self.watermark_file = self.watermark_path = None

        # we accept PIL Image objects, file-like objects or file paths
        if isinstance(watermark, Image.Image):
            self.watermark_image = watermark
        elif hasattr(watermark, "read") and callable(watermark.open):
            self.watermark_file = watermark
        elif isinstance(watermark, basestring):
            self.watermark_path = watermark
        else:
            raise TypeError("watermark must be a PIL Image, file-like object or "
                            "a path")