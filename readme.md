# classify images from a webcam

## about

The photos can be distinguished in *too bright*, *too dark*, *with a lot of red* (because of UV lamp) and *good photos*.
First we need to get rid of the too bright ones because they show nothing significant.
Later we may want to classify the other types for better time lapse videos.

## process

(1) categorise some photos using shotwell into 4 ratings (named above).
(2) add some image manipulation functions to calculate hue.
(3) train using i.e. Tensorflow
(4) Profit.
