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
<iframe id="myIframe" src="FILEHERE" width=100% height=1000 style="border:none">

</iframe>

<script>
function injectDarkCSS(iframe) {
  try {
    const doc = iframe.contentDocument || iframe.contentWindow.document;
    if (!doc) return;

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

// 如果 iframe 还没加载完
iframe.addEventListener('load', () => injectDarkCSS(iframe));

// 如果 iframe 已经加载完，也可以直接调用
// injectDarkCSS(iframe);
</script>
""".replace("FILEHERE",file)