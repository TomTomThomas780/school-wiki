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
<div id="loadingTip">加载中…</div>
<iframe id="myIframe" src="FILEHERE" width=100% height=1000 style="border:none;display:none">
</iframe>

<style>
  #loadingTip {
    height: 1000px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #888;
    font-size: 14px;
  }
  @media (prefers-color-scheme: dark) {
    #loadingTip { color: #aaa; background: #111; }
  }
</style>

<script>
function injectDarkCSS(iframe) {
  try {
    const doc = iframe.contentDocument || iframe.contentWindow.document;
    if (!doc || !doc.head) return;

    const style = doc.createElement('style');
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
  } catch (e) {
    console.warn('无法注入 iframe CSS，可能是跨域：', e);
  }
}

const iframe = document.getElementById('myIframe');

iframe.addEventListener('load', () => {
  injectDarkCSS(iframe);
  document.getElementById('loadingTip').remove();
  iframe.style.display = 'block';
});
</script>
""".replace("FILEHERE",file)