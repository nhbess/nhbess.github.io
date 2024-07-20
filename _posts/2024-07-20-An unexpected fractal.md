---
layout: post
title: An unexpected fractal
image: "/assets/images/post_pics/An unexpected fractal/13.jpg"
---

Some time ago I wrote a program for visualizing search algorithms in a grid. A relatively simple [Breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search)that mutate its color on each search depth over a grid.

Nice plots. Extremely slow.

<table>
  <tr>
    <td><img src="assets/images/post_pics/An unexpected fractal/10.jpg" alt="Alt text 1" style="max-width: 100px; max-height: 100px;"></td>
    <td><img src="https://via.placeholder.com/150" alt="Alt text 2" style="max-width: 100px; max-height: 100px;"></td>
    <td><img src="https://via.placeholder.com/150" alt="Alt text 3" style="max-width: 100px; max-height: 100px;"></td>
  </tr>
  <tr>
    <td><img src="https://via.placeholder.com/150" alt="Alt text 4" style="max-width: 100px; max-height: 100px;"></td>
    <td><img src="https://via.placeholder.com/150" alt="Alt text 5" style="max-width: 100px; max-height: 100px;"></td>
    <td><img src="https://via.placeholder.com/150" alt="Alt text 6" style="max-width: 100px; max-height: 100px;"></td>
  </tr>
</table>
So I tried to rewrite it in a more efficient fashion, but somewhere on the process I made a mistake in the code, and there it was: an unexpected fractal suddenly appeared.

