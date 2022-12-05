<h1 class="gap">0x01. Plotting</h1>

<h2>Learning Objectives</h2>

<ul>
<li>What is a plot?</li>
<li>What is a scatter plot? line graph? bar graph? histogram?</li>
<li>What is <code>matplotlib</code>?</li>
<li>How to plot data with <code>matplotlib</code></li>
<li>How to label a plot</li>
<li>How to scale an axis</li>
<li>How to plot multiple sets of data at the same time</li>
</ul>

<h2>Requirements</h2>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.8)</li>
<li>Your files will be executed with <code>numpy</code> (version 1.19.2) and <code>matplotlib</code> (version 3.3.4)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.6)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>Unless otherwise noted, you are not allowed to import any module</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>


<h2 class="gap">Tasks</h2>
<h2 class="panel-title">
      0. Line Graph
    </h3>
<p>Complete the following source code to plot <code>y</code> as a line graph:</p>
<ul>
<li><code>y</code> should be plotted as a solid red line</li>
<li>The x-axis should range from 0 to 10</li>
</ul>
<img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/664b2543b48ef4918687.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T171435Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2e9475c26550256082d25af8c4ef1d833e0c6f3e1580e21cb4df66ee351195f7" alt="" style="">

<h2 class="panel-title">
      1. Scatter
    </h3>

<p>Complete the following source code to plot <code>x ↦ y</code> as a scatter plot:</p>
<ul>
<li>The x-axis should be labeled <code>Height (in)</code></li>
<li>The y-axis should be labeled <code>Weight (lbs)</code></li>
<li>The title should be <code>Men's Height vs Weight</code></li>
<li>The data should be plotted as magenta points</li>
</ul>
<pre><code>#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

### your code here
</code></pre>
<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/1b143961d254e65afa2c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T171435Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c0d7c749116cc0501d7349141c3e74dd6cf877d0688fc9082705f8d2ce1a95d8" alt="" style=""></p>

<h2 class="panel-title">
      2. Change of scale
    </h3>

<p>Complete the following source code to plot <code>x ↦ y</code> as a line graph:</p>

<ul>
<li>The x-axis should be labeled <code>Time (years)</code></li>
<li>The y-axis should be labeled <code>Fraction Remaining</code></li>
<li>The title should be <code>Exponential Decay of C-14</code></li>
<li>The y-axis should be logarithmically scaled</li>
<li>The x-axis should range from 0 to 28650</li>
</ul>

<pre><code>#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# your code here
</code></pre>

<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/9/2b6334feb069ae1b6014.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221205%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20221205T171435Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=61eb111dc1c42a60ac6a90c4e8189b096030d78e160b5db6affff82289ecfb32" alt="" loading="lazy" style=""></p>

  </div>



<h2>Resources</h2>
<h3>Installing Matplotlib 3.3.4</h3>
<pre><code>pip install --user matplotlib==3.3.4
pip install --user Pillow
sudo apt-get install python3-tk
</code></pre>
<p>To check that it has been successfully downloaded, use <code>pip list</code>.</p>
<h3>Configure X11 Forwarding</h3>
<p>Update your <code>Vagrantfile</code> to include the following:</p>
<pre><code>Vagrant.configure(2) do |config|
  ...
  config.ssh.forward_x11 = true
end
</code></pre>
<p>If you are running <code>vagrant</code> on a Mac, you will have to install <a href="/rltoken/OVdbL0nPcj2IXiTQoIBwAw" title="XQuartz" target="_blank">XQuartz</a> and restart your computer.</p>

<p>If you are running <code>vagrant</code> on a Windows computer, you may have to follow <a href="/rltoken/ZGU33rI2v1sPC_WvoXukkg" title="these instructions" target="_blank">these instructions</a>.</p>

<p>Once complete, you should simply be able to <code>vagrant ssh</code> to log into your VM and then any GUI application should forward to your local machine.</p>

<p><em>Hint for <code>emacs</code> users: you will have to use <code>emacs -nw</code> to prevent it from launching its GUI.</em></p>


<p><strong>Read or watch</strong>:</p>
<ul>
<li><a href="/rltoken/U-55m7o6No-_W4OJP-oTCg" title="Plot (graphics)" target="_blank">Plot (graphics)</a> </li>
<li><a href="/rltoken/ewQvwktgrnrccqp9PInBpQ" title="Scatter plot" target="_blank">Scatter plot</a> </li>
<li><a href="/rltoken/nUnDxiEeIAMxoV0Vk9dsOg" title="Line chart" target="_blank">Line chart</a> </li>
<li><a href="/rltoken/YZcEmsWNuQcQXYqzfyBfPg" title="Bar chart" target="_blank">Bar chart</a> </li>
<li><a href="/rltoken/7icFpl6tgO6OvwSvee0S2Q" title="Histogram" target="_blank">Histogram</a> </li>
</ul>
<p><strong>References</strong>:</p>
<ul>
<li><a href="/rltoken/9GES4KAFhBUOKYj9BI9vgQ" title="Pyplot tutorial" target="_blank">Pyplot tutorial</a> </li>
<li><a href="/rltoken/GaHr4hgXE3LE3skZDGH2pQ" title="matplotlib.pyplot" target="_blank">matplotlib.pyplot</a> </li>
<li><a href="/rltoken/IUhQVdCg4MaCdUFEOuaXig" title="matplotlib.pyplot.plot" target="_blank">matplotlib.pyplot.plot</a> </li>
<li><a href="/rltoken/oZ9O1frltXpknQLJGalGPg" title="matplotlib.pyplot.scatter" target="_blank">matplotlib.pyplot.scatter</a> </li>
<li><a href="/rltoken/gqW7RjVdB5G3WtuzJTcdew" title="matplotlib.pyplot.bar" target="_blank">matplotlib.pyplot.bar</a> </li>
<li><a href="/rltoken/K-yG7lADPJCb_FSWyOGerA" title="matplotlib.pyplot.hist" target="_blank">matplotlib.pyplot.hist</a> </li>
<li><a href="/rltoken/jhcagbtOr5Xq98SmXs8WTQ" title="matplotlib.pyplot.xlabel" target="_blank">matplotlib.pyplot.xlabel</a> </li>
<li><a href="/rltoken/jxrkMnJZTqhaRuvfIal5hQ" title="matplotlib.pyplot.ylabel" target="_blank">matplotlib.pyplot.ylabel</a> </li>
<li><a href="/rltoken/5yPCtvA_2CSecHenfen8cQ" title="matplotlib.pyplot.title" target="_blank">matplotlib.pyplot.title</a> </li>
<li><a href="/rltoken/ex_hmQCXTo2gHAbUFfPTyw" title="matplotlib.pyplot.subplot" target="_blank">matplotlib.pyplot.subplot</a> </li>
<li><a href="/rltoken/3465mnzNsJp36kpDEd7tCA" title="matplotlib.pyplot.subplots" target="_blank">matplotlib.pyplot.subplots</a> </li>
<li><a href="/rltoken/6AIYCbwzqy67xdvhSzj1Aw" title="matplotlib.pyplot.subplot2grid" target="_blank">matplotlib.pyplot.subplot2grid</a> </li>
<li><a href="/rltoken/S5YwnEoLjpTYGDz5VryX6w" title="matplotlib.pyplot.suptitle" target="_blank">matplotlib.pyplot.suptitle</a> </li>
<li><a href="/rltoken/Gy6aJCznMv4uSNn2LWS6rg" title="matplotlib.pyplot.xscale" target="_blank">matplotlib.pyplot.xscale</a> </li>
<li><a href="/rltoken/XmLFrfjIS2WnwnjumbHLrg" title="matplotlib.pyplot.yscale" target="_blank">matplotlib.pyplot.yscale</a> </li>
<li><a href="/rltoken/1zKdiptFjaMmbv8iqBVY1Q" title="matplotlib.pyplot.xlim" target="_blank">matplotlib.pyplot.xlim</a> </li>
<li><a href="/rltoken/NDvu8opoi1B_uhJjB8SA0g" title="matplotlib.pyplot.ylim" target="_blank">matplotlib.pyplot.ylim</a> </li>
<li><a href="/rltoken/ENFsqb4q1lbSwCEUgTAt0Q" title="mplot3d tutorial" target="_blank">mplot3d tutorial</a> </li>
<li><a href="/rltoken/-4sdqeB5ey_3u3htSZZQpw" title="additional tutorials" target="_blank">additional tutorials</a> </li>
</ul>







## Authors
<a href="https://www.linkedin.com/in/kadzahk/?locale=en_US">Kadzahk</a> [![M](https://cdn.icon-icons.com/icons2/1753/PNG/32/iconfinder-social-media-applications-14linkedin-4102586_113786.png)](https://www.linkedin.com/in/kadzahk/?locale=en_US)