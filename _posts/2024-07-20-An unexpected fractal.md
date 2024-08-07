---
layout: post
title: An unexpected fractal
image: "/assets/images/post_pics/an_unexpected_fractal/13.jpg"
---

Some time ago I wrote a program for visualizing search algorithms in a grid. A relatively simple [Breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search) that mutates its color on each search depth over a grid.

Nice plots. Extremely slow.

<table>
  <tr>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/0.jpg" alt="Image 0" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>       
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/1.jpg" alt="Image 1" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>       
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/10.jpg" alt="Image 2" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>      
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/11.jpg" alt="Image 3" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>      
  </tr>
  <tr>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/12.jpg" alt="Image 4" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>      
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/13.jpg" alt="Image 5" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>      
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/14.jpg" alt="Image 6" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>      
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/15.jpg" alt="Image 7" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>      
  </tr>
  <tr>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/16.jpg" alt="Image 8" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/17.jpg" alt="Image 9" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/18.jpg" alt="Image 10" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/19.jpg" alt="Image 11" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>
  <tr>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/2.jpg" alt="Image 12" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/3.jpg" alt="Image 13" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/4.jpg" alt="Image 14" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/5.jpg" alt="Image 15" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>
  <tr>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/6.jpg" alt="Image 16" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/7.jpg" alt="Image 17" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/8.jpg" alt="Image 18" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
    <td><img src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/9.jpg" alt="Image 19" style="max-width: 200px; max-height: 200px; width: 100%; height: auto;"></td>
  </tr>
</table>


So I tried to rewrite it in a more efficient fashion, but somewhere on the process I made a mistake in the code, and there it was: an unexpected fractal suddenly appeared.

<table>
  <tr>
    <td>
      <video autoplay loop controls style=" height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/small_0.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video autoplay loop controls style=" height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/small_1.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video autoplay loop controls style=" height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/small_2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video autoplay loop controls style=" height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/small_3.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
  </tr>
</table>

This is a centered view, the 'square shape' repeats as it grows. I still don't know what went wrong, but I'm happy with the result.

<table>
  <tr>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/centered.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
  </tr>
  <tr>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/centered2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
  </tr>
</table>

### Galery
I decided that before fixing the bug I would make a few more tests. Funny thing is that when changing the kernel (neighborhood) the fractal nature is conserved, presumably linear transformations of a fractal transformation are indeed fractals. Here are some of the results for different kernels and number of seeds.

<table>
  <tr>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav0.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav1.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav10.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
  </tr>
  <tr>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav11.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav12.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav13.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
  </tr>
  <tr>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav14.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav15.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav16.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
  </tr>
  <tr>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav17.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav18.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
  </tr>
  <tr>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav3.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav4.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav5.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
  </tr>
  <tr>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav6.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav7.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
    <td>
      <video controls style="height: 200px; width: auto;">
        <source src="{{ site.baseurl }}/assets/images/post_pics/an_unexpected_fractal/fav8.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </td>
  </tr>
</table>
