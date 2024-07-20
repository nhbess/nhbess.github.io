---
layout: post
title: An unexpected fractal
image: "/assets/images/post_pics/An unexpected fractal/13.jpg"
---

Some time ago I wrote a program for visualizing search algorithms in a grid. A relatively simple [Breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search) that mutate its color on each search depth over a grid.

Nice plots. Extremely slow.

<table>
  <tr>
    <td><img src= "18.jpg" alt="Alt text 1" style="width:100;  height: auto"></td>
  </tr>
  <tr>
    <td><img src= /assets/images/animation_550.gif alt="Alt text 6" style="max-width: 200px; max-height: 200px;"></td>
    <td><img src= animation_550.gif alt="Alt text 6" style="max-width: 200px; max-height: 200px;"></td>
  </tr>
</table>

![[animation_550.gif]]

So I tried to rewrite it in a more efficient fashion, but somewhere on the process I made a mistake in the code, and there it was: an unexpected fractal suddenly appeared.

