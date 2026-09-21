API 参考 / RouterLinkProps
# 接口：RouterLinkProps 
## 继承关系 
RouterLinkOptions
↳ RouterLinkProps
## 属性 
### activeClass 
• 可选 activeClass: string
链接在匹配当前路由时被应用到 class。
### ariaCurrentValue 
• 可选 ariaCurrentValue: "location" | "time" | "page" | "step" | "date" | "true" | "false"
链接在匹配当前路由时传入 aria-current attribute 的值。
Default Value
'page'
### custom 
• 可选 custom: boolean
RouterLink 是否应该将其内容包裹在一个 a 标签里。用于通过 v-slot 创建自定义 RouterLink。
### exactActiveClass 
• 可选 exactActiveClass: string
链接在严格匹配当前路由时被应用到 class。
### replace 
• 可选 replace: boolean
调用 router.replace 以替换 router.push。
#### 继承自 
RouterLinkOptions.replace
### to 
• to: RouteLocationRaw
当点击该链接时应该进入的路由地址。
#### 继承自 
RouterLinkOptions.to