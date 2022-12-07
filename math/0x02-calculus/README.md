

<h1>0x02. Calculus</h1>

<h2>Learning Objectives</h2>

<ul>
<li>Summation and Product notation</li>
<li>What is a series?</li>
<li>Common series</li>
<li>What is a derivative?</li>
<li>What is the product rule?</li>
<li>What is the chain rule?</li>
<li>Common derivative rules</li>
<li>What is a partial derivative?</li>
<li>What is an indefinite integral?</li>
<li>What is a definite integral?</li>
<li>What is a double integral?</li>
</ul>
<h2>Requirements</h2>
<h3>Multiple Choice Questions</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>Type the number of the correct answer in your answer file</li>
<li>All your files should end with a new line</li>
</ul>
<p>Example:</p>
<p>What is 9 squared?</p>

<ol>
<li>99</li>
<li>81</li>
<li>3</li>
<li>18</li>
</ol>
<pre><code>alexa@ubuntu$ cat answer_file
2
alexa@ubuntu$
</code></pre>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 16.04 LTS using <code>python3</code> (version 3.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>pycodestyle</code> style (version 2.5)</li>
<li>All your modules should have documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>Unless otherwise noted, you are not allowed to import any module</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>




<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a href="/rltoken/skg3vK5GnKDlmbo06Z39kg" title="Sigma Notation" target="_blank">Sigma Notation</a> (<em>starting at 0:32</em>)</li>
<li><a href="/rltoken/1s_bEA6qmWwQdyCdS57p6Q" title="Π Product Notation" target="_blank">Π Product Notation</a> (<em>up to 0:20</em>)</li>
<li><a href="/rltoken/ZspTKBdWZlHNerawd9D4Sg" title="Sigma and Pi Notation" target="_blank">Sigma and Pi Notation</a> </li>
<li><a href="/rltoken/WKUeLXtYGtgy6-aeGkJLlw" title="What is a Series?" target="_blank">What is a Series?</a> </li>
<li><a href="/rltoken/IdeBjxt81rWtmzw6_M49Cw" title="What is a Mathematical Series?" target="_blank">What is a Mathematical Series?</a> </li>
<li><a href="/rltoken/naVPzDDoc9jPnbYkHquwvg" title="List of mathematical series: Sums of powers" target="_blank">List of mathematical series: Sums of powers</a> </li>
<li><a href="/rltoken/fat5s_d4dwYZA0Yte4t-Uw" title="Bernoulli Numbers(Bn)" target="_blank">Bernoulli Numbers(Bn)</a> </li>
<li><a href="/rltoken/lnZW-G4HDu2_lnqmSeqRHQ" title="Bernoulli Polynomials(Bn(x))" target="_blank">Bernoulli Polynomials(Bn(x))</a> </li>
<li><a href="/rltoken/_-viHILcipzP7jCvnyg4rA" title="Derivative (mathematics)" target="_blank">Derivative (mathematics)</a> </li>
<li><a href="/rltoken/eCFsGe67mLMGBMa7s0Xr5Q" title="Calculus for ML" target="_blank">Calculus for ML</a> </li>
<li><a href="/rltoken/cjMjHONX-9OvvNVuJJ287g" title="1 of 2: Seeing the big picture" target="_blank">1 of 2: Seeing the big picture</a> </li>
<li><a href="/rltoken/TiiWVCiTvesA-3St-leH9g" title="2 of 2: First Principles" target="_blank">2 of 2: First Principles</a> </li>
<li><a href="/rltoken/O04dmG-51DuicnMwaZEkjA" title="1 of 2: Finding the Derivative" target="_blank">1 of 2: Finding the Derivative</a> </li>
<li><a href="/rltoken/1rmJr_DwEwo7tcuQ-LoqeA" title="2 of 2: What do we discover?" target="_blank">2 of 2: What do we discover?</a> </li>
<li><a href="/rltoken/nLQHib0sX2z73jKzD4oKwA" title="Deriving a Rule for Differentiating Powers of x" target="_blank">Deriving a Rule for Differentiating Powers of x</a> </li>
<li><a href="/rltoken/TJWR0t3PjWti2UrbcdB7eA" title="1 of 3: Introducing a substitution" target="_blank">1 of 3: Introducing a substitution</a> </li>
<li><a href="/rltoken/UjpV5Ddf19ltOg88kWi1CQ" title="2 of 3: Combining derivatives" target="_blank">2 of 3: Combining derivatives</a> </li>
<li><a href="/rltoken/ZCQFq3Q3KIMH91C3LYLXnw" title="How To Understand Derivatives: The Product, Power &amp; Chain Rules" target="_blank">How To Understand Derivatives: The Product, Power &amp; Chain Rules</a> </li>
<li><a href="/rltoken/OLTns7QVN7B_t2exxA0Veg" title="Product Rule" target="_blank">Product Rule</a> </li>
<li><a href="/rltoken/oQzY3Fn3thW6gmEidiIvkg" title="Common Derivatives and Integrals" target="_blank">Common Derivatives and Integrals</a> </li>
<li><a href="/rltoken/LZCUUvV4lDJygZ9L7l_cmA" title="Introduction to partial derivatives" target="_blank">Introduction to partial derivatives</a> </li>
<li><a href="/rltoken/KFO0jdqRSP0VdcbQH8Bi5g" title="Partial derivatives - How to solve?" target="_blank">Partial derivatives - How to solve?</a> </li>
<li><a href="/rltoken/re8znLNlhEfp4N3r-JeOAQ" title="Integral" target="_blank">Integral</a></li>
<li><a href="/rltoken/pgGn7hNWnrGyRL8CToSc5A" title="Integration and the fundamental theorem of calculus" target="_blank">Integration and the fundamental theorem of calculus</a></li>
<li><a href="/rltoken/17TxJkRzKof53LNoo8qjnQ" title="Introduction to Integration" target="_blank">Introduction to Integration</a></li>
<li><a href="/rltoken/eKOysHn5yjSKVB5nqGwFgQ" title="Indefinite Integral - Basic Integration Rules, Problems, Formulas, Trig Functions, Calculus" target="_blank">Indefinite Integral - Basic Integration Rules, Problems, Formulas, Trig Functions, Calculus</a></li>
<li><a href="/rltoken/8YLPWRz_eCNLniUUQM33Bw" title="Definite Integrals" target="_blank">Definite Integrals</a></li>
<li><a href="/rltoken/Jf1fpX0RVNkmC2FBIb-Y4Q" title="Definite Integral" target="_blank">Definite Integral</a></li>
<li><a href="/rltoken/i3MWqee_18vmpDQi-iek6w" title="Multiple integral" target="_blank">Multiple integral</a></li>
<li><a href="/rltoken/lxFcfHmuexAmnFu7r9M-8Q" title="Double integral 1" target="_blank">Double integral 1</a></li>
<li><a href="/rltoken/j25rQN7u1uC3qkM4fAGpCg" title="Double integrals 2" target="_blank">Double integrals 2</a></li>
</ul>




## Authors
<a href="https://www.linkedin.com/in/kadzahk/?locale=en_US">Kadzahk</a> [![M](https://cdn.icon-icons.com/icons2/1753/PNG/32/iconfinder-social-media-applications-14linkedin-4102586_113786.png)](https://www.linkedin.com/in/kadzahk/?locale=en_US)