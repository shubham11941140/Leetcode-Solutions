<h2> 345 50
3333. Find the Original Typed String II</h2><hr><div><p>Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and <strong>may</strong> press a key for too long, resulting in a character being typed <strong>multiple</strong> times.</p>

<p>You are given a string <code>word</code>, which represents the <strong>final</strong> output displayed on Alice's screen. You are also given a <strong>positive</strong> integer <code>k</code>.</p>

<p>Return the total number of <em>possible</em> original strings that Alice <em>might</em> have intended to type, if she was trying to type a string of size <strong>at least</strong> <code>k</code>.</p>

<p>Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "aabbccdd", k = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The possible strings are: <code>"aabbccdd"</code>, <code>"aabbccd"</code>, <code>"aabbcdd"</code>, <code>"aabccdd"</code>, and <code>"abbccdd"</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "aabbccdd", k = 8</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The only possible string is <code>"aabbccdd"</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word = "aaabbb", k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>word</code> consists only of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 2000</code></li>
</ul>
</div>