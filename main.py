import os
def define_env(env):

    @env.macro
    def status_auth(status:str):
        match status:
            case "teacher":
                return """
!!! note

    本文主要由教师撰写

     
"""
            case "fromTeacher":
                return """
!!! note

    本文由编者根据教师提供的资料撰写

    
"""
            case "student":
                return """

!!! warning

    本文主要由编者撰写


"""

    @env.macro
    def html_refer(file:str):
        return r"""
<<div class="iframe-wrap">
  <iframe id="myIframe" src="FILEHERE" width="100%" height="1000" style="border:none"></iframe>
  <div id="loadingTip" class="loading-tip">加载中…</div>
</div>

<style>
  .iframe-wrap {
    position: relative;
    width: 100%;
    height: 1000px;
  }

  .iframe-wrap iframe {
    display: block;
    width: 100%;
    height: 1000px;
    border: none;
    background: #f4f7f7;
  }

  .loading-tip {
    position: absolute;
    top: 0; left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    z-index: 10;
    transition: opacity .25s;
    /* 跟随 MkDocs 主题背景色 / 次要文字色 */
    background: var(--md-default-bg-color, #f4f7f7);
    color: var(--md-default-fg-color--light, #888);
  }

  .loading-tip.is-hide {
    opacity: 0;
    pointer-events: none;
  }

  /* 已删除 @media (prefers-color-scheme: dark) 里的遮罩颜色，
     因为变量会自动跟随 MkDocs 主题切换 */
</style>

<script>
(function () {
  function injectDarkCSS(iframe) {
    try {
      const doc = iframe.contentDocument || iframe.contentWindow.document;
      if (!doc || !doc.head) return false;
      if (doc.getElementById('__dark_css__')) return true;

      const style = doc.createElement('style');
      style.id = '__dark_css__';
      style.textContent = `
        @media screen and (prefers-color-scheme: dark) {
          body { background: #111; }
          .wrap { filter: invert(1) hue-rotate(180deg);}
          .pic, .matwrap { filter: hue-rotate(180deg) invert(1); }
        }
      `;
      doc.head.appendChild(style);
      return true;
    } catch (e) {
      console.warn('无法注入 iframe CSS，可能是跨域：', e);
      return false;
    }
  }

  const iframe = document.getElementById('myIframe');
  const tip = document.getElementById('loadingTip');
  if (!iframe || !tip) return;

  const start = Date.now();
  const MIN_SHOW = 300;

  let finished = false;

  function finish() {
    if (finished) return;
    finished = true;

    const wait = Math.max(0, MIN_SHOW - (Date.now() - start));
    setTimeout(() => {
      tip.classList.add('is-hide');
      setTimeout(() => tip.remove(), 300);
    }, wait);
  }

  const timer = setInterval(() => {
    const doc = iframe.contentDocument || iframe.contentWindow.document;
    if (!doc || !doc.head) return;

    injectDarkCSS(iframe);

    const bodyReady = doc.body && doc.body.children.length > 0;
    if (doc.getElementById('__dark_css__') && bodyReady) {
      clearInterval(timer);
      requestAnimationFrame(() => requestAnimationFrame(finish));
    }
  }, 10);

  iframe.addEventListener('load', () => {
    clearInterval(timer);
    injectDarkCSS(iframe);
    requestAnimationFrame(() => requestAnimationFrame(finish));
  });
})();
</script>""".replace("FILEHERE",file)