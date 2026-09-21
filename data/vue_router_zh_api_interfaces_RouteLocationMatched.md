API 参考 / RouteLocationMatched
# 接口：RouteLocationMatched 
一条路由记录的规范化版本。
## 继承关系 
RouteRecordNormalized
↳ RouteLocationMatched
## 属性 
### aliasOf 
• aliasOf: undefined | RouteRecordNormalized
定义了是否这条记录是另一条的别名。如果记录是原始记录，则该属性为 undefined。
#### 继承自 
RouteRecordNormalized.aliasOf
### beforeEnter 
• beforeEnter: undefined | NavigationGuardWithThis<undefined> | NavigationGuardWithThis<undefined>[]
被注册的 beforeEnter 守卫
#### 继承自 
RouteRecordNormalized.beforeEnter
### children 
• children: RouteRecordRaw[]
嵌套的路由记录。
#### 继承自 
RouteRecordNormalized.children
### components 
• components: undefined | null | Record<string, RouteComponent>
{@inheritDoc RouteRecordMultipleViews.components}
#### Override 
RouteRecordNormalized.components
### instances 
• instances: Record<string, undefined | null | ComponentPublicInstance>
Mounted route component instance。 Having the instances on the record mean beforeRouteUpdate and beforeRouteLeave guards can only be invoked with the latest mounted app instance if there are multiple application instances rendering the same view, basically duplicating the content on the page, which shouldn't happen in practice. It will work if multiple apps are rendering different named views.
#### 继承自 
RouteRecordNormalized.instances
### meta 
• meta: RouteMeta
Arbitrary data attached to the record.
#### 继承自 
RouteRecordNormalized.meta
### name 
• name: undefined | RouteRecordName
Name for the route record. Must be unique.
#### 继承自 
RouteRecordNormalized.name
### path 
• path: string
Path of the record. Should start with / unless the record is the child of another record.
#### 继承自 
RouteRecordNormalized.path
### props 
• props: Record<string, _RouteRecordProps>
Allow passing down params as props to the component rendered by router-view. Should be an object with the same keys as components or a boolean to be applied to every component.
#### 继承自 
RouteRecordNormalized.props
### redirect 
• redirect: undefined | RouteRecordRedirectOption
Where to redirect if the route is directly matched. The redirection happens before any navigation guard and triggers a new navigation with the new target location.
#### 继承自 
RouteRecordNormalized.redirect