API 参考 / RouteLocationNormalizedLoaded
# 接口：RouteLocationNormalizedLoaded 
RouteLocationRaw with
## 继承关系 
_RouteLocationBase
↳ RouteLocationNormalizedLoaded
## 属性 
### fullPath 
• fullPath: string
包括 search 和 hash 在内的完整地址。该字符串是经过百分号编码的。
#### 继承自 
_RouteLocationBase.fullPath
### hash 
• hash: string
当前地址的 hash。如果存在则以 # 开头。
#### 继承自 
_RouteLocationBase.hash
### matched 
• matched: RouteLocationMatched[]
RouteLocationMatched 数组，只包含直接的组件 (任何已被加载并在 components 对象内被替换掉的懒加载组件)。所以它可以被直接用于展示路由。同样它不包含重定向的记录。
### meta 
• meta: RouteMeta
从所有匹配的路由记录中合并的 meta 属性。
#### 继承自 
_RouteLocationBase.meta
### name 
• name: undefined | null | RouteRecordName
匹配的路由名称。
#### 继承自 
_RouteLocationBase.name
### params 
• params: RouteParams
从 path 中提取出来并解码后的参数对象。
#### 继承自 
_RouteLocationBase.params
### path 
• path: string
经过百分号编码的 URL 中的 pathname 段。
#### 继承自 
_RouteLocationBase.path
### query 
• query: LocationQuery
代表当前地址的 search 属性的对象
#### 继承自 
_RouteLocationBase.query
### redirectedFrom 
• redirectedFrom: undefined | RouteLocation
包含在重定向到当前地址之前，我们最初想访问的地址。
#### 继承自 
_RouteLocationBase.redirectedFrom