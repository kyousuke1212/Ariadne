# 组件基础 
组件允许我们将 UI 划分为独立的、可重用的部分，并且可以对每个部分进行单独的思考。在实际应用中，组件常常被组织成一个层层嵌套的树状结构：
!展示组件树结构的图示，根组件分支出多个子组件和嵌套的子子组件
这和我们嵌套 HTML 元素的方式类似，Vue 实现了自己的组件模型，使我们可以在每个组件内封装自定义内容与逻辑。Vue 同样也能很好地配合原生 Web Component。如果你想知道 Vue 组件与原生 Web Components 之间的关系，可以阅读此章节。
## 定义一个组件 
当使用构建步骤时，我们一般会将 Vue 组件定义在一个单独的 .vue 文件中，这被叫做单文件组件 (简称 SFC)：
vue

export default {
data() {
return {
count: 0
}
}
}


You clicked me {{ count }} times.


vue

import { ref } from 'vue'
const count = ref(0)


You clicked me {{ count }} times.


当不使用构建步骤时，一个 Vue 组件以一个包含 Vue 特定选项的 JavaScript 对象来定义：
js
export default {
data() {
return {
count: 0
}
},
template: 

You clicked me {{ count }} times.

}

js
import { ref } from 'vue'
export default {
setup() {
const count = ref(0)
return { count }
},
template: 

You clicked me {{ count }} times.

// 也可以针对一个 DOM 内联模板：
// template: '#my-template-element'
}

这里的模板是一个内联的 JavaScript 字符串，Vue 将会在运行时编译它。你也可以使用 ID 选择器来指向一个元素 (通常是原生的  元素)，Vue 将会使用其内容作为模板来源。
上面的例子中定义了一个组件，并在一个 .js 文件里默认导出了它自己，但你也可以通过具名导出在一个文件中导出多个组件。
## 使用组件 
我们会在接下来的指引中使用单文件组件语法，无论你是否使用构建步骤，组件相关的概念都是相同的。示例一节中展示了两种场景中的组件使用情况。
要使用一个子组件，我们需要在父组件中导入它。假设我们把计数器组件放在了一个叫做 ButtonCounter.vue 的文件中，这个组件将会以默认导出的形式被暴露给外部。
vue

import ButtonCounter from './ButtonCounter.vue'
export default {
components: {
ButtonCounter
}
}


Here is a child component!



若要将导入的组件暴露给模板，我们需要在 components 选项上注册它。这个组件将会以其注册时的名字作为模板中的标签名。
vue

import ButtonCounter from './ButtonCounter.vue'


Here is a child component!



通过 ，导入的组件都在模板中直接可用。
当然，你也可以全局地注册一个组件，使得它在当前应用中的任何组件上都可以使用，而不需要额外再导入。关于组件的全局注册和局部注册两种方式的利弊，我们放在了组件注册这一章节中专门讨论。
组件可以被重用任意多次：
vue-html
Here is a child component!




在演练场中尝试一下
在演练场中尝试一下
你会注意到，每当点击这些按钮时，每一个组件都维护着自己的状态，是不同的 count。这是因为每当你使用一个组件，就创建了一个新的实例。
在单文件组件中，推荐为子组件使用 PascalCase 的标签名，以此来和原生的 HTML 元素作区分。虽然原生 HTML 标签名是不区分大小写的，但 Vue 单文件组件是可以在编译中区分大小写的。我们也可以使用 /> 来关闭一个标签。
如果你是直接在 DOM 中书写模板 (例如原生  元素的内容)，模板的编译需要遵从浏览器中 HTML 的解析行为。在这种情况下，你应该需要使用 kebab-case 形式并显式地关闭这些组件的标签。
vue-html





请看 DOM 内模板解析注意事项了解更多细节。
## 传递 props 
如果我们正在构建一个博客，我们可能需要一个表示博客文章的组件。我们希望所有的博客文章分享相同的视觉布局，但有不同的内容。要实现这样的效果自然必须向组件中传递数据，例如每篇文章标题和内容，这就会使用到 props。
Props 是一种特别的 attributes，你可以在组件上声明注册。要传递给博客文章组件一个标题，我们必须在组件的 props 列表上声明它。这里要用到 props 选项defineProps 宏：
vue [BlogPost.vue]

export default {
props: ['title']
}


{{ title }}


当一个值被传递给 prop 时，它将成为该组件实例上的一个属性。该属性的值可以像其他组件属性一样，在模板和组件的 this 上下文中访问。
vue [BlogPost.vue]

defineProps(['title'])


{{ title }}


defineProps 是一个仅  中可用的编译宏命令，并不需要显式地导入。声明的 props 会自动暴露给模板。defineProps 会返回一个对象，其中包含了可以传递给组件的所有 props：
js
const props = defineProps(['title'])
console.log(props.title)

TypeScript 用户请参考：为组件 props 标注类型
如果你没有使用 ，props 必须以 props 选项的方式声明，props 对象会作为 setup() 函数的第一个参数被传入：
js
export default {
props: ['title'],
setup(props) {
console.log(props.title)
}
}

一个组件可以有任意多的 props，默认情况下，所有 prop 都接受任意类型的值。
当一个 prop 被注册后，可以像这样以自定义 attribute 的形式传递数据给它：
vue-html




在实际应用中，我们可能在父组件中会有如下的一个博客文章数组：
js
export default {
// ...
data() {
return {
posts: [
{ id: 1, title: 'My journey with Vue' },
{ id: 2, title: 'Blogging with Vue' },
{ id: 3, title: 'Why Vue is so fun' }
]
}
}
}

js
const posts = ref([
{ id: 1, title: 'My journey with Vue' },
{ id: 2, title: 'Blogging with Vue' },
{ id: 3, title: 'Why Vue is so fun' }
])

这种情况下，我们可以使用 v-for 来渲染它们：
vue-html
<BlogPost
v-for="post in posts"
:key="post.id"
:title="post.title"
/>

在演练场中尝试一下
在演练场中尝试一下
留意我们是如何使用 v-bind 语法 (:title="post.title") 来传递动态 prop 值的。当事先不知道要渲染的确切内容时，这一点特别有用。
以上就是目前你需要了解的关于 props 的全部了。如果你看完本章节后还想知道更多细节，我们推荐你深入阅读关于 props 的完整指引。
## 监听事件 
让我们继续关注我们的  组件。我们会发现有时候它需要与父组件进行交互。例如，要在此处实现无障碍访问的需求，将博客文章的文字能够放大，而页面的其余部分仍使用默认字号。
在父组件中，我们可以添加一个 postFontSize 数据属性ref 来实现这个效果：
js{6}
data() {
return {
posts: [
/* ... */
],
postFontSize: 1
}
}

js{5}
const posts = ref([
/* ... */
])
const postFontSize = ref(1)

在模板中用它来控制所有博客文章的字体大小：
vue-html{1,7}

<BlogPost
v-for="post in posts"
:key="post.id"
:title="post.title"
/>


然后，给  组件添加一个按钮：
vue{5} [BlogPost.vue]
 -->


{{ title }}
Enlarge text



这个按钮目前还没有做任何事情，我们想要点击这个按钮来告诉父组件它应该放大所有博客文章的文字。要解决这个问题，组件实例提供了一个自定义事件系统。父组件可以通过 v-on 或 @ 来选择性地监听子组件上抛的事件，就像监听原生 DOM 事件那样：
vue-html{3}
<BlogPost
...
@enlarge-text="postFontSize += 0.1"
/>

子组件可以通过调用内置的 $emit 方法，通过传入事件名称来抛出一个事件：
vue{5} [BlogPost.vue]
 -->


{{ title }}
Enlarge text



因为有了 @enlarge-text="postFontSize += 0.1" 的监听，父组件会接收这一事件，从而更新 postFontSize 的值。
在演练场中尝试一下
在演练场中尝试一下
我们可以通过 emits 选项defineEmits 宏来声明需要抛出的事件：
vue{4} [BlogPost.vue]

export default {
props: ['title'],
emits: ['enlarge-text']
}


vue{3} [BlogPost.vue]

defineProps(['title'])
defineEmits(['enlarge-text'])


这声明了一个组件可能触发的所有事件，还可以对事件的参数进行验证。同时，这还可以让 Vue 避免将它们作为原生事件监听器隐式地应用于子组件的根元素。
和 defineProps 类似，defineEmits 仅可用于  之中，并且不需要导入，它返回一个等同于 $emit 方法的 emit 函数。它可以被用于在组件的  中抛出事件，因为此处无法直接访问 $emit：
vue

const emit = defineEmits(['enlarge-text'])
emit('enlarge-text')


TypeScript 用户请参考：为组件 emits 标注类型
如果你没有在使用 ，你可以通过 emits 选项定义组件会抛出的事件。你可以从 setup() 函数的第二个参数，即 setup 上下文对象上访问到 emit 函数：
js
export default {
emits: ['enlarge-text'],
setup(props, ctx) {
ctx.emit('enlarge-text')
}
}

以上就是目前你需要了解的关于组件自定义事件的所有知识了。如果你看完本章节后还想知道更多细节，请深入阅读组件事件章节。
## 通过插槽来分配内容 
一些情况下我们会希望能和 HTML 元素一样向组件中传递内容：
vue-html

Something bad happened.


我们期望能渲染成这样：
Something bad happened.
这可以通过 Vue 的自定义  元素来实现：
vue{4} [AlertBox.vue]


This is an Error for Demo Purposes




.alert-box {
/* ... */
}


如上所示，我们使用  作为一个占位符，父组件传递进来的内容就会渲染在这里。
在演练场中尝试一下
在演练场中尝试一下
以上就是目前你需要了解的关于插槽的所有知识了。如果你看完本章节后还想知道更多细节，请深入阅读组件插槽章节。
## 动态组件 
有些场景会需要在两个组件间来回切换，比如 Tab 界面：
在演练场中查看示例
在演练场中查看示例
上面的例子是通过 Vue 的  元素和特殊的 is attribute 实现的：
vue-html



vue-html



在上面的例子中，被传给 :is 的值可以是以下几种：
* 被注册的组件名
* 导入的组件对象
你也可以使用 is attribute 来创建一般的 HTML 元素。
当使用  来在多个组件间作切换时，被切换掉的组件会被卸载。我们可以通过  组件强制被切换掉的组件仍然保持“存活”的状态。
## DOM 内模板解析注意事项 
如果你想在 DOM 中直接书写 Vue 模板，Vue 则必须从 DOM 中获取模板字符串。由于浏览器的原生 HTML 解析行为限制，有一些需要注意的事项。
请注意下面讨论只适用于直接在 DOM 中编写模板的情况。如果你使用来自以下来源的字符串模板，就不需要顾虑这些限制了：
* 单文件组件
* 内联模板字符串 (例如 template: '...')
* 
### 大小写区分 
HTML 标签和属性名称是不分大小写的，所以浏览器会把任何大写的字符解释为小写。这意味着当你使用 DOM 内的模板时，无论是 PascalCase 形式的组件名称、camelCase 形式的 prop 名称还是 v-on 的事件名称，都需要转换为相应等价的 kebab-case (短横线连字符) 形式：
js
// JavaScript 中的 camelCase
const BlogPost = {
props: ['postTitle'],
emits: ['updatePost'],
template: 
{{ postTitle }}

}

vue-html



### 闭合标签 
我们在上面的例子中已经使用过了闭合标签 (self-closing tag)：
vue-html


这是因为 Vue 的模板解析器支持任意标签使用 /> 作为标签关闭的标志。
然而在 DOM 内模板中，我们必须显式地写出关闭标签：
vue-html


这是由于 HTML 只允许一小部分特殊的元素省略其关闭标签，最常见的就是  和 。对于其他的元素来说，如果你省略了关闭标签，原生的 HTML 解析器会认为开启的标签永远没有结束，用下面这个代码片段举例来说：
vue-html
 
hello

将被解析为：
vue-html

hello
 

### 元素位置限制 
某些 HTML 元素对于放在其中的元素类型有限制，例如 ，， 和 ，相应的，某些元素仅在放置于特定元素中时才会显示，例如 ， 和 。
这将导致在使用带有此类限制元素的组件时出现问题。例如：
vue-html




自定义的组件  将作为无效的内容被忽略，因而在最终呈现的输出中造成错误。我们可以使用特殊的 is attribute 作为一种解决方案：
vue-html




当使用在原生 HTML 元素上时，is 的值必须加上前缀 vue: 才可以被解析为一个 Vue 组件。这一点是必要的，为了避免和原生的自定义内置元素相混淆。
以上就是你需要了解的关于 DOM 内模板解析的所有注意事项，同时也是 Vue *基础*部分的所有内容。祝贺你！虽然还有很多需要学习的，但你可以先暂停一下，去用 Vue 做一些有趣的东西，或者研究一些示例。
完成了本页的阅读后，回顾一下你刚才所学到的知识，如果还想知道更多细节，我们推荐你继续阅读关于组件的完整指引。