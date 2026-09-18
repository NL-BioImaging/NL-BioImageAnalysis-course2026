
## Remarks Day 1: Jupyter Notebooks Martijn

### General

- [X] Add links to the (API reference) websites of skimage, scipy etc. E.g. https://scikit-image.org/docs/stable/api/api.html, or https://docs.scipy.org/doc/scipy/reference/ndimage.html
    - (MW) I added the two links above, for **future edition** might be nice to check again which links are most relevant.

### Part I
- [X] Triangle threshold code block still uses `thresh_otsu`.
    - (MW) Fixed.
- [ ] The Triangle explanation image is huge <img ... width=400> apparently doesn't always work
    - (MW) Mm, I don't see this behavior, and don't know how to fix. Check this for **future editions**.

### Part II
- [ ] Background correction:
	- [X] 'Correct with a constant' and 'Common approaches: use the mode, average of known background region.' together are a single list item. Same for 'Estimate the background pattern, which is likely more coarse-grained' and 'Approaches: Rolling ball'.
        - (MW:) Addressed by itemizing differently. (I hope this is what you meant.) This section is not very mature, for **future editions** could develop this more. (Also using Bram's materials eg.)
	- [ ] Mode doesn't always find the best background, especially with confocal data. It works well here though.
        - (MW:) Background subtraction is not my strong suite, so might be nice to chat about this later. 
	- [X] I don't really agree with the way the background is subtracted. By setting everything lower than the mode to 0 you alter measurements. Why not convert to floating point? (Again, in this case you probably measure only already positive numbers, so it won't be a problem, but this may not always be the case.)
        - (MW:) I agree float conversion is better and data shouldn't be thrown away. I do wonder how one would make sure ratios don't end up becoming negative (that result is equally invalid as zero for this particular use case). I guess anyways division by zero is currently also possible, so both approaches need special/edge case handling.

### Part III
- [X] There is a (future) deprecation warning from `sk.morphology.remove_small_objects()`, but the documentation is then also not up to date: https://scikit-image.org/docs/0.25.x/api/skimage.morphology.html#skimage.morphology.remove_small_objects
Using `max_size` works as well, without any warnings.
    - (MW:) Used `max_size`
- [ ] The exercise asks a lot from the students. It will probably take a long time, and they may need hints.
    - (MW:) Agreed, I added some hints, but it's still very hard for python beginners. Can be addressed more for **future editions**.
