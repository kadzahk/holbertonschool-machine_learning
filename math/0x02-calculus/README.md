<h1 class="gap">0x03. Probability</h1>
<h2>Learning Objectives</h2>
<ul>
<li>What is probability?</li>
<li>Basic probability notation</li>
<li>What is independence? What is disjoint?</li>
<li>What is a union? intersection?</li>
<li>What are the general addition and multiplication rules?</li>
<li>What is a probability distribution?</li>
<li>What is a probability distribution function? probability mass function?</li>
<li>What is a cumulative distribution function?</li>
<li>What is a percentile?</li>
<li>What is mean, standard deviation, and variance?</li>
<li>Common probability distributions</li>
</ul>
<h2>Requirements</h2>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.8)</li>
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
<h2>Mathematical Approximations</h2>
<p>For the following tasks, you will have to use various irrational numbers and functions. Since you are not able to import any libraries, please use the following approximations:</p>
<ul>
<li><em>π</em> = 3.1415926536</li>
<li><em>e</em> = 2.7182818285</li>
<li><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2019/4/5e71204ca545072e8766.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20221212%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20221212T195058Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=0e6198665a775e05e7d03a3002de03b4d54375e72ff1a42fdc50bac0d3f7fd3d" alt="" loading="lazy" style=""></li>
</ul>
<h2>Resources</h2>
<ul>
<li><a href="/rltoken/ZggoiEvv6Yi28ddpDdRf5A" title="Probability" target="_blank">Probability</a></li>
<li><a href="/rltoken/lvFWzxi6ojQN6kLhQ4t-JQ" title="Basic Concepts" target="_blank">Basic Concepts</a></li>
<li><a href="/rltoken/d3V6VMIBciqUciimA0uG7g" title="Intro to probability 1: Basic notation" target="_blank">Intro to probability 1: Basic notation</a></li>
<li><a href="/rltoken/q-lZzr4Y2ACNzE-P4W0v1Q" title="Intro to probability 2: Independent and disjoint" target="_blank">Intro to probability 2: Independent and disjoint</a></li>
<li><a href="/rltoken/_AYQ5zzBgJ8AaZRHUIj4sw" title="Intro to Probability 3: General Addition Rule; Union; OR" target="_blank">Intro to Probability 3: General Addition Rule; Union; OR</a></li>
<li><a href="/rltoken/v5eLcUN_15IraTYt_LmHIA" title="Intro to Probability 4: General multiplication rule; Intersection; AND" target="_blank">Intro to Probability 4: General multiplication rule; Intersection; AND</a></li>
<li><a href="/rltoken/Kkt4DwrZ5H3LSGePVqt1Aw" title="Permutations and Combinations" target="_blank">Permutations and Combinations</a></li>
<li><a href="/rltoken/42CEUdBffkNdfw0_xtidWw" title="Probability distribution" target="_blank">Probability distribution</a></li>
<li><a href="/rltoken/VcXrRJ8P_x0VvscNlOZ6SQ" title="Probability Theory" target="_blank">Probability Theory</a></li>
<li><a href="/rltoken/1rQ3Is5znPPsP__vso935w" title="Cumulative Distribution Functions" target="_blank">Cumulative Distribution Functions</a></li>
<li><a href="/rltoken/Igose8HXOpWt_J2bRN7Ipg" title="Common Probability Distributions: The Data Scientist’s Crib Sheet" target="_blank">Common Probability Distributions: The Data Scientist’s Crib Sheet</a></li>
<li><a href="/rltoken/B1qQQHvRWmWFRYMPEdXmUg" title="NORMAL MODEL PART 1 --- EMPIRICAL RULE" target="_blank">NORMAL MODEL PART 1 — EMPIRICAL RULE</a></li>
<li><a href="/rltoken/COhfVdgzwr78gFqWPoj9fQ" title="Normal Distribution" target="_blank">Normal Distribution</a></li>
<li><a href="/rltoken/dsXzwQ3vLRrmZhy60Ciqyw" title="Variance" target="_blank">Variance</a></li>
<li><a href="/rltoken/tvnDhgxyEVovjx68hWTGWA" title="Variance (Concept)" target="_blank">Variance (Concept)</a></li>
<li><a href="/rltoken/ee8T1XQR0QAlkLjPlCdWRQ" title="Binomial Distribution" target="_blank">Binomial Distribution</a></li>
<li><a href="/rltoken/56XvG5Sd6HDRVMXiaJiWwQ" title="Poisson Distribution" target="_blank">Poisson Distribution</a></li>
<li><a href="/rltoken/fg0s82pFqiryvZPeM1UN3Q" title="Hypergeometric Distribution" target="_blank">Hypergeometric Distribution</a></li>
</ul>







## Authors
<a href="https://www.linkedin.com/in/kadzahk/?locale=en_US">Kadzahk</a> [![M](https://cdn.icon-icons.com/icons2/1753/PNG/32/iconfinder-social-media-applications-14linkedin-4102586_113786.png)](https://www.linkedin.com/in/kadzahk/?locale=en_US)