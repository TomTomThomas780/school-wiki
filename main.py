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
    def phrase(phrase:str):
        fphrase=phrase.replace(" ","_")
        if os.path.exists(f".\\docs\\english\\phrase\\{fphrase}.md"):
            return f"[phrase](/english/phrase/{fphrase})"
        return f"{phrase}"

    @env.macro
    def word(word:str):
        fword=word.replace(" ","_")
        if os.path.exists(f".\\docs\\english\\word\\{fword}.md"):
            return f"[phrase](/english/phrase/{fword})"
        return f"{word}"
        