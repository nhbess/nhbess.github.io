---
layout: post
title: An unexpected fractal
image: "/assets/images/post_pics/An unexpected fractal/13.jpg"
---

Some time ago I wrote a program for visualizing search algorithms in a grid. A relatively simple [Breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search)that mutate its color on each search depth over a grid.

Nice plots. Extremely slow.

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px;">
  <img src="assets/images/post_pics/An unexpected fractal/0.jpg" alt="Image 1" style="width: 100%; max-width: 200px; object-fit: cover;">   
  <img src="assets/images/post_pics/An unexpected fractal/1.jpg" alt="Image 2" style="width: 100%; max-width: 200px; object-fit: cover;">   
  <img src="assets/images/post_pics/An unexpected fractal/10.jpg" alt="Image 3" style="width: 100%; max-width: 200px; object-fit: cover;">  
</div>

So I tried to rewrite it in a more efficient fashion, but somewhere on the process I made a mistake in the code, and there it was: an unexpected fractal suddenly appeared.

