API 参考 / NavigationFailure
# 接口：NavigationFailure 
Error 类型的扩展，包含导航失败的额外信息。
## 继承关系 
Error
↳ NavigationFailure
## 属性 
### cause 
• 可选 cause: unknown
#### 继承自 
Error.cause
### from 
• from: RouteLocationNormalized
上一个路由位置
### message 
• message: string
#### 继承自 
Error.message
### name 
• name: string
#### 继承自 
Error.name
### stack 
• 可选 stack: string
#### 继承自 
Error.stack
### to 
• to: RouteLocationNormalized
要导航至的下一个路由位置
### type 
• type: NAVIGATION_ABORTED | NAVIGATION_CANCELLED | NAVIGATION_DUPLICATED
导航类型。属于 NavigationFailureType 的一种。