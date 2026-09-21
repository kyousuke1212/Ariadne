API 参考 / NavigationFailureType
# 枚举：NavigationFailureType 
为导航失败枚举所有可能的类型。可以传入 isNavigationFailure 以检查特定的失败情况。
## 枚举成员 
### aborted 
• aborted = 4
中断的导航是因为导航守卫返回 false 会调用了 next(false) 而导致失败的导航。
### cancelled 
• cancelled = 8
取消的导航是因为另一个更近的导航已经开始 (不需要完成) 而导致失败的导航。
### duplicated 
• duplicated = 16
重复的导航是因为其开始的时候已经处在相同的路径而导致失败的导航。