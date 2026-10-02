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
<script>
function injectDarkCSS(iframe) {
  try {
    const doc = iframe.contentDocument || iframe.contentWindow.document;
    if (!doc || !doc.head) return false;
    if (doc.getElementById('__dark_css__')) return true;

    const style = doc.createElement('style');
    style.id = '__dark_css__';
    style.textContent = `
     @media screen and (prefers-color-scheme: dark) {
  body {
    background: #111;
  }

  .wrap {
    filter: invert(1) hue-rotate(180deg);
    background: #fff;
  }

  .pic {
    filter: hue-rotate(180deg) invert(1);
  }
  .matwrap {
    filter: hue-rotate(180deg) invert(1);
  }
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
let done = false;

function finish() {
  if (done) return;
  done = true;
  const tip = document.getElementById('loadingTip');
  if (tip) tip.remove();
  // 双 rAF：确保注入的样式已经重算并应用到 iframe 内部
  requestAnimationFrame(() => requestAnimationFrame(() => {
    iframe.style.display = 'block';
  }));
}

// 轮询只负责尽早注入样式，不触发显示
const timer = setInterval(() => {
  injectDarkCSS(iframe);
}, 10);

// 等所有资源加载完，再注入一次并显示
iframe.addEventListener('load', () => {
  clearInterval(timer);
  injectDarkCSS(iframe);
  finish();
});
</script>""".replace("FILEHERE",file)