API 参考 / Router
# 接口：Router 
路由器实例。
## 属性 
### currentRoute 
• 只读 currentRoute: Ref<RouteLocationNormalizedLoaded>
当前的 RouteLocationNormalized。
### listening 
• listening: boolean
允许关闭历史事件的监听器。这是一个为微前端提供的底层 API。
### options 
• 只读 options: RouterOptions
创建路由器时的原始选项对象。
## Methods 
### addRoute 
▸ addRoute(parentName, route): () => void
添加一个新的路由记录，将其作为一个已有路由的子路由。
#### 参数 
名称 |
类型 |
描述 |
parentName |
RouteRecordName |
route 应该被加入到的父级路由记录 |
route |
RouteRecordRaw |
要加入的路由记录 |
#### 返回值 
fn
▸ (): void
添加一个新的路由记录，将其作为一个已有路由的子路由。
返回值 
void
▸ addRoute(route): () => void
添加一个新的路由记录到该路由器中。
#### 参数 
名称 |
类型 |
描述 |
route |
RouteRecordRaw |
要加入的路由记录 |
#### 返回值 
fn
▸ (): void
添加一个新的路由记录到该路由器中。
返回值 
void
### afterEach 
▸ afterEach(guard): () => void
添加一个导航守卫，它会在每次导航之后被执行。返回一个用来移除该钩子的函数。
#### 参数 
名称 |
类型 |
描述 |
guard |
NavigationHookAfter |
要加入的导航守卫 |
#### 返回值 
fn
a function that removes the registered hook
▸ (): void
添加一个导航守卫，它会在每次导航之后被执行。返回一个用来移除该钩子的函数。
Example
```
jsrouter.afterEach((to, from, failure) => {
  if (isNavigationFailure(failure)) {
    console.log('failed navigation', failure)
  }
})
```
返回值 
void
### back 
▸ back(): void
通过调用 history.back() 在可能的情况下在历史中后退。相当于 router.go(-1)。
#### 返回值 
void
### beforeEach 
▸ beforeEach(guard): () => void
添加一个导航守卫，它会在每次导航之前被执行。返回一个用来移除该钩子的函数。
#### 参数 
名称 |
类型 |
描述 |
guard |
NavigationGuardWithThis<undefined> |
要加入的导航守卫 |
#### 返回值 
fn
▸ (): void
添加一个导航守卫，它会在每次导航之前被执行。返回一个用来移除该钩子的函数。
返回值 
void
### beforeResolve 
▸ beforeResolve(guard): () => void
添加一个导航守卫，它会在导航将要被解析之前被执行。此时所有组件都已经获取完毕，且其它导航守卫也都已经完成调用。返回一个用来移除该守卫的函数。
#### 参数 
名称 |
类型 |
描述 |
guard |
NavigationGuardWithThis<undefined> |
要加入的导航守卫 |
#### 返回值 
fn
▸ (): void
添加一个导航守卫，它会在导航将要被解析之前被执行。此时所有组件都已经获取完毕，且其它导航守卫也都已经完成调用。返回一个用来移除该守卫的函数。
Example
```
jsrouter.beforeResolve(to => {
  if (to.meta.requiresAuth && !isAuthenticated) return false
})
```
返回值 
void
### forward 
▸ forward(): void
通过调用 history.forward() 在可能的情况下在历史中前进。相当于 router.go(1)。
#### 返回值 
void
### getRoutes 
▸ getRoutes(): RouteRecordNormalized[]
获得所有路由记录的完整列表。
#### 返回值 
RouteRecordNormalized[]
### go 
▸ go(delta): void
允许你在历史中前进或后退。相当于 router.go()。
#### 参数 
名称 |
类型 |
描述 |
delta |
number |
相对于当前页面你想要移动到的历史中的位置 |
#### 返回值 
void
### hasRoute 
▸ hasRoute(name): boolean
检查一个给定名称的路由是否存在。
#### 参数 
名称 |
类型 |
描述 |
name |
RouteRecordName |
要检查的路由名称 |
#### 返回值 
boolean
### isReady 
▸ isReady(): Promise<void>
返回一个 Promise，它会在路由器完成初始导航之后被解析，也就是说这时所有和初始路由有关联的异步入口钩子和异步组件都已经被解析。如果初始导航已经发生，则该 Promise 会被立刻解析。
这在服务端渲染中确认服务端和客户端输出一致的时候非常有用。注意在服务端你需要手动加入初始地址，而在客户端，路由器会从 URL 中自动获取。
#### 返回值 
Promise<void>
### onError 
▸ onError(handler): () => void
添加一个错误处理器，它会在每次导航遇到未被捕获的错误出现时被调用。其中包括同步和异步被抛出的错误、在任何导航守卫中返回或传入 next 的错误、尝试解析一个需要渲染路由的异步组件时发生的错误。
#### 参数 
名称 |
类型 |
描述 |
handler |
_ErrorListener |
要注册的错误处理器 |
#### 返回值 
fn
▸ (): void
添加一个错误处理器，它会在每次导航遇到未被捕获的错误出现时被调用。其中包括同步和异步被抛出的错误、在任何导航守卫中返回或传入 next 的错误、尝试解析一个需要渲染路由的异步组件时发生的错误。
返回值 
void
### push 
▸ push(to): Promise<undefined | void | NavigationFailure>
程序式地通过将一条记录加入到历史栈中来导航到一个新的 URL。
#### 参数 
名称 |
类型 |
描述 |
to |
RouteLocationRaw |
要导航到的路由 |
#### 返回值 
Promise<undefined | void | NavigationFailure>
### removeRoute 
▸ removeRoute(name): void
根据其名称移除一个现有的路由。
#### 参数 
名称 |
类型 |
描述 |
name |
RouteRecordName |
要移除的路由名称 |
#### 返回值 
void
### replace 
▸ replace(to): Promise<undefined | void | NavigationFailure>
程序式地通过替换历史栈中的当前记录来导航到一个新的 URL。
#### 参数 
名称 |
类型 |
描述 |
to |
RouteLocationRaw |
要导航到的路由 |
#### 返回值 
Promise<undefined | void | NavigationFailure>
### resolve 
▸ resolve(to, currentLocation?): RouteLocation & { href: string }
返回一个路由地址的规范化版本。同时包含一个包含任何现有 base 的 href 属性。默认情况下，用于 router.currentRoute 的 currentLocation 应该在特别高阶的用例下才会被覆写。
#### 参数 
名称 |
类型 |
描述 |
to |
RouteLocationRaw |
要解析的原始路由地址 |
currentLocation? |
RouteLocationNormalizedLoaded |
可选的被解析的当前地址 |
#### 返回值 
RouteLocation & { href: string }