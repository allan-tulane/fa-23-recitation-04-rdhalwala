# CMPS 2200 Reciation 5
## Answers

**Name:**___Raiya Dhalwala______________________


Place all written answers from `recitation-05.md` here for easier grading.







- **1b.**

The running time for fixed pivot quicksort was almsot linear, so comparatively terrible compared to the theoretical quicksort runtime. The random pivot runtime was much better than the fixed pivot runtime, but was still close to the worst case asymptotically as it was exponential. As the list size grew, so did the runtime for all functions. 

|      n |   qsort-fixed-pivot |   qsort-random-pivot |   tim_sort |
|--------|---------------------|----------------------|------------|
|    100 |               0.157 |                0.285 |      0.011 |
|    200 |               0.340 |                0.408 |      0.018 |
|    500 |               1.055 |                1.171 |      0.049 |
|   1000 |               3.443 |                3.100 |      0.105 |
|   2000 |              18.769 |                9.644 |      0.246 |
|   5000 |              46.303 |               27.486 |      0.670 |
|  10000 |              27.152 |               69.580 |      1.709 |
|  20000 |             106.728 |              167.249 |      4.313 |
|  50000 |             267.062 |              465.985 |      8.710 |
| 100000 |             702.096 |              778.210 |     25.068 |


- **1c.**

tim_sort was much faster than quicksort. It was better than quicksort random pivot as well.