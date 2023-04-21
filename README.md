<!-- Title -->
<h1 align="center">WinZard</h1>

<!-- Logo -->
<p align="center">
  <img src="https://github.com/MegaFocusDev/WinZard/blob/main/Winzard.png" alt="WinZard Logo">
</p>

<!-- Description -->
<p align="center">
  WinZard is an open source and simple tool for Windows that provides a customizable shortcut button on your keyboard for clearing your clipboard quickly.
</p>

<!-- Table of Contents -->
<h2>Table of Contents</h2>

<ul>
  <li><a href="#requirements">Requirements</a></li>
  <li><a href="#installation">Installation</a></li>
	<li><a href="#usage">Usage</a></li>
	<li><a href="#customization">Customization</a></li>
	<li><a href="#uninstallation">Uninstallation</a></li>
	<li><a href="#license">License</a></li>
</ul>

<h2 id="requirements">Requirements</h2>
<p>WinZard requires Python 3 and the following packages, which can be installed by running <code>pip install -r requirements.txt</code> in a command prompt:</p>
<ul>
	<li>keyboard</li>
	<li>pyperclip</li>
</ul>

<!-- Installation -->
<h2 id=“installation”>Installation</h2>

<p>To install WinZard, follow these steps:</p>
<ol>

<li>Download the latest release of WinZard from the <a href=“https://github.com/MegaFocusDev/WinZard/releases”>Releases</a> page on GitHub.</li>

<li>Extract the ZIP archive to a directory of your choice.</li>

<li>Open a terminal or command prompt and navigate to the directory where you extracted the files.</li>

<li>Verify that Python 3 is installed on your system by running the command <code>python --version</code>.</li>

<li>Once you’ve verified that Python 3 is installed on your system, run the command <code>python winzard.pyw</code> to start WinZard. If this is your first time running WinZard, you may need to run it as an administrator in order for it to work properly.</li>

<li>Great job, you’re all set. From now on, you won’t have to worry about running WinZard every time you start up your computer.</li>

<p><strong>Tip:</strong> If you wish to disable WinZard from running on computer startup, you can easily do so from the Task Manager by navigating to the Startup tab and disabling the WinZard program from the list.</p>

</ol>

<!-- Usage -->
<h2 id="usage">Usage</h2>

<p>
  Once WinZard is installed, it runs in the background and provides a shortcut button on your keyboard to clear your clipboard quickly. The default shortcut key is <kbd>Ctrl</kbd> + <kbd>End</kbd>.
</p>

<!-- Customization -->
<h2 id="customization">Customization</h2>

<p>
  WinZard allows you to customize the shortcut key by editing the <code>shortcut_key</code> variable in the <code>winzard.pyw</code> file. Simply open the <code>winzard.pyw</code> file using a code editor, locate the <code>shortcut_key</code> variable near the top of the file, and change the value to the desired shortcut key.
</p>

<h2 id="uninstallation">Uninstallation</h2>
<p>Uninstalling WinZard is very easy. To remove the program from your system, simply delete the <code>winzard.pyw</code> file from the directory where you extracted the files. That’s it!</p>

<!-- License -->
<h2 id="license">License</h2>

<p>
  This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.
</p>
