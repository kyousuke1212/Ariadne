# 命名路由 
在 Vue School 上观看免费视频课程
当创建一个路由时，我们可以选择给路由一个 name：
```
jsconst routes = [
  {
    path: '/user/:username',
    name: 'profile', 
    component: User,
  },
]
```
然后我们可以使用 name 而不是 path 来传递 to 属性给 <router-link>：
```
template<router-link :to="{ name: 'profile', params: { username: 'erina' } }">
  User profile
</router-link>
```
上述示例将创建一个指向 /user/erina 的链接。
- 在演练场上查看。
使用 name 有很多优点：
- 没有硬编码的 URL。
- params 的自动编码/解码。
- 防止你在 URL 中出现打字错误。
- 绕过路径排序，例如展示一个匹配相同路径但排序较低的路由。
✨自信地编写 Vue 应用的 Vibe 代码RuleKit
所有路由的命名都必须是唯一的。如果为多条路由添加相同的命名，路由器只会保留最后那一条。你可以在动态路由章节了解更多。
Vue Router 有很多其他部分可以传入网址，例如 router.push() 和 router.replace() 方法。我们将在编程式导航指南中详细介绍这些方法。就像 to 属性一样，这些方法也支持通过 name 传入网址：
```
jsrouter.push({ name: 'user', params: { username: 'erina' } })
```