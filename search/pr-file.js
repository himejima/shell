// github のPRのページを開いて、コンソールで実行してください
[...document.querySelectorAll('.file-info>a')].map(x => x.title)
.map(x => x)
.join('\n')
