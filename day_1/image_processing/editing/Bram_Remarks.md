
## Remarks Day 1: Jupyter Notebooks Martijn

General: Add links to the (API reference) websites of skimage, scipy etc. E.g. https://scikit-image.org/docs/stable/api/api.html, or https://docs.scipy.org/doc/scipy/reference/ndimage.html

### Part I
- Triangle threshold code block still uses `thresh_otsu`.
- The Triangle explanation image is huge <img ... width=400> apparently doesn't always work

### Part II
- Background correction:
	- 'Correct with a constant' and 'Common approaches: use the mode, average of known background region.' together are a single list item. Same for 'Estimate the background pattern, which is likely more coarse-grained' and 'Approaches: Rolling ball'.
	- Mode doesn't always find the best background, especially with confocal data. It works well here though.
	- I don't really agree with the way the background is subtracted. By setting everything lower than the mode to 0 you alter measurements. Why not convert to floating point? (Again, in this case you probably measure only already positive numbers, so it won't be a problem, but this may not always be the case.)

### Part III
- There is a (future) deprecation warning from `sk.morphology.remove_small_objects()`, but the documentation is then also not up to date: https://scikit-image.org/docs/0.25.x/api/skimage.morphology.html#skimage.morphology.remove_small_objects
Using `max_size` works as well, without any warnings.
- The exercise asks a lot from the students. It will probably take a long time, and they may need hints.
