---
layout: post
title: An unexpected fractal
image: "/assets/images/post_pics/An unexpected fractal/13.jpg"
---

Some time ago I wrote a program for visualizing search algorithms in a grid. A relatively simple [Breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search) that mutate its color on each search depth over a grid.

Nice plots. Extremely slow.

<table>
  <tr>
    <td><img src=an_unexpected_fractal_0.jpg alt="Image 0" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_1.jpg alt="Image 1" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_10.jpg alt="Image 2" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_11.jpg alt="Image 3" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>
  <tr>
    <td><img src=an_unexpected_fractal_12.jpg alt="Image 4" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_13.jpg alt="Image 5" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_14.jpg alt="Image 6" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_15.jpg alt="Image 7" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>
  <tr>
    <td><img src=an_unexpected_fractal_16.jpg alt="Image 8" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_17.jpg alt="Image 9" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_18.jpg alt="Image 10" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_19.jpg alt="Image 11" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>
  <tr>
    <td><img src=an_unexpected_fractal_2.jpg alt="Image 12" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_3.jpg alt="Image 13" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_4.jpg alt="Image 14" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_5.jpg alt="Image 15" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>
  <tr>
    <td><img src=an_unexpected_fractal_6.jpg alt="Image 16" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_7.jpg alt="Image 17" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_8.jpg alt="Image 18" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src=an_unexpected_fractal_9.jpg alt="Image 19" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>
</table>
So I tried to rewrite it in a more efficient fashion, but somewhere on the process I made a mistake in the code, and there it was: an unexpected fractal suddenly appeared.


![Alt text](an_unexpected_fractal_9.jpg)

<img src="an_unexpected_fractal_9.jpg" alt="Alt text" style="width:50%;">
![Alt text]({{ site.baseurl }}/assets/images/example.gif)

<img src=an_unexpected_fractal_9.jpg alt="Alt text" style="width:50%;">
![Alt text]({{ site.baseurl }}/assets/images/example.gif)

<img src="{{ site.baseurl }}/assets/images/example.gif" alt="Alt text" style="width:50%;">
