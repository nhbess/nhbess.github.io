---
layout: post
title: An unexpected fractal
image: "/assets/images/post_pics/An unexpected fractal/13.jpg"
---

Some time ago I wrote a program for visualizing search algorithms in a grid. A relatively simple [Breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search) that mutate its color on each search depth over a grid.

Nice plots. Extremely slow.


<table>
  <tr>
    <td><img src="{{ site.baseurl }}/assets/images/example.gif" alt="Image 3" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>
  <tr>
    <td><img src=an_unexpected_fractal_15.jpg alt="Image 7" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>
  <tr>
    <td><img src="{{ site.baseurl }}/assets/images/GIF.gif" alt="Image 16" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>
</table>


  <tr>
    <td><img src="{{ site.baseurl }}/assets/images/GIF.gif" alt="Image 16" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>


So I tried to rewrite it in a more efficient fashion, but somewhere on the process I made a mistake in the code, and there it was: an unexpected fractal suddenly appeared.

<img src="{{ site.baseurl }}/assets/images/example.gif" alt="Alt text" style="width:50%;">
