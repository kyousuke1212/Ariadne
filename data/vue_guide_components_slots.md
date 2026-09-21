# 插槽 Slots 
> 此章节假设你已经看过了组件基础。若你还不了解组件是什么，请先阅读该章节。
## 插槽内容与出口 
在之前的章节中，我们已经了解到组件能够接收任意类型的 JavaScript 值作为 props，但组件要如何接收模板内容呢？在某些场景中，我们可能想要为子组件传递一些模板片段，让子组件在它们的组件中渲染这些片段。
举例来说，这里有一个  组件，可以像这样使用：
vue-html{2}

Click me! 


而  的模板是这样的：
vue-html{2}

 


 元素是一个插槽出口 (slot outlet)，标示了父元素提供的插槽内容 (slot content) 将在哪里被渲染。
!展示父组件的插槽内容被注入到子组件插槽出口的图示
最终渲染出的 DOM 是这样：
html
Click me!

在演练场中尝试一下
在演练场中尝试一下
通过使用插槽， 仅负责渲染外层的  (以及相应的样式)，而其内部的内容由父组件提供。
理解插槽的另一种方式是和下面的 JavaScript 函数作类比，其概念是类似的：
js
// 父元素传入插槽内容
FancyButton('Click me!')
// FancyButton 在自己的模板中渲染插槽内容
function FancyButton(slotContent) {
return 
${slotContent}

}

插槽内容可以是任意合法的模板内容，不局限于文本。例如我们可以传入多个元素，甚至是组件：
vue-html

Click me!



在演练场中尝试一下
在演练场中尝试一下
通过使用插槽， 组件更加灵活和具有可复用性。现在组件可以用在不同的地方渲染各异的内容，但同时还保证都具有相同的样式。
Vue 组件的插槽机制是受原生 Web Component  元素的启发而诞生，同时还做了一些功能拓展，这些拓展的功能我们后面会学习到。
## 渲染作用域 
插槽内容可以访问到父组件的数据作用域，因为插槽内容本身是在父组件模板中定义的。举例来说：
vue-html
{{ message }}
{{ message }}

这里的两个 {{ message }} 插值表达式渲染的内容都是一样的。
插槽内容无法访问子组件的数据。Vue 模板中的表达式只能访问其定义时所处的作用域，这和 JavaScript 的词法作用域规则是一致的。换言之：
> 父组件模板中的表达式只能访问父组件的作用域；子组件模板中的表达式只能访问子组件的作用域。
## 默认内容 
在外部没有提供任何内容的情况下，可以为插槽指定默认内容。比如有这样一个  组件：
vue-html




如果我们想在父组件没有提供任何插槽内容时在  内渲染“Submit”，只需要将“Submit”写在  标签之间来作为默认内容：
vue-html{3}


Submit 



现在，当我们在父组件中使用  且没有提供任何插槽内容时：
vue-html


“Submit”将会被作为默认内容渲染：
html
Submit

但如果我们提供了插槽内容：
vue-html
Save

那么被显式提供的内容会取代默认内容：
html
Save

在演练场中尝试一下
在演练场中尝试一下
## 具名插槽 
有时在一个组件中包含多个插槽出口是很有用的。举例来说，在一个  组件中，有如下模板：
vue-html












对于这种场景， 元素可以有一个特殊的 attribute name，用来给各个插槽分配唯一的 ID，以确定每一处要渲染的内容：
vue-html












这类带 name 的插槽被称为具名插槽 (named slots)。没有提供 name 的  出口会隐式地命名为“default”。
在父组件中使用  时，我们需要一种方式将多个插槽内容传入到各自目标插槽的出口。此时就需要用到具名插槽了：
要为具名插槽传入内容，我们需要使用一个含 v-slot 指令的  元素，并将目标插槽的名字传给该指令：
vue-html






v-slot 有对应的简写 #，因此  可以简写为 。其意思就是“将这部分模板片段传入子组件的 header 插槽中”。
!展示布局组件中多个具名插槽，父组件内容被分发到对应的 header、main 和 footer 插槽的图示
下面我们给出完整的、向  传递插槽内容的代码，指令均使用的是缩写形式：
vue-html


Here might be a page title


A paragraph for the main content.
And another one.


Here's some contact info



当一个组件同时接收默认插槽和具名插槽时，所有位于顶级的非  节点都被隐式地视为默认插槽的内容。所以上面也可以写成：
vue-html


Here might be a page title


A paragraph for the main content.
And another one.

Here's some contact info



现在  元素中的所有内容都将被传递到相应的插槽。最终渲染出的 HTML 如下：
html


Here might be a page title


A paragraph for the main content.
And another one.


Here's some contact info



在演练场中尝试一下
在演练场中尝试一下
使用 JavaScript 函数来类比可能更有助于你来理解具名插槽：
js
// 传入不同的内容给不同名字的插槽
BaseLayout({
header: ...,
default: ...,
footer: ...
})
//  渲染插槽内容到对应位置
function BaseLayout(slots) {
return 
${slots.header}
${slots.default}
${slots.footer}

}

## 条件插槽 
有时你需要根据内容是否被传入了插槽来渲染某些内容。
你可以结合使用 $slots 属性与 v-if 来实现。
在下面的示例中，我们定义了一个卡片组件，它拥有三个条件插槽：header、footer 和 default。
当 header、footer 或 default 的内容存在时，我们希望包装它以提供额外的样式：
vue-html














在演练场中尝试一下
## 动态插槽名 
动态指令参数在 v-slot 上也是有效的，即可以定义下面这样的动态插槽名：
vue-html


...



...



注意这里的表达式和动态指令参数受相同的语法限制。
## 作用域插槽 
在上面的渲染作用域中我们讨论到，插槽的内容无法访问到子组件的状态。
然而在某些场景下插槽的内容可能想要同时使用父组件域内和子组件域内的数据。要做到这一点，我们需要一种方法来让子组件在渲染时将一部分数据提供给插槽。
事实上，我们确实可以这样做——可以像向组件传递 props 一样，向一个插槽的出口上传递 attributes。父级模板通过 v-slot 接收插槽 props，而子级模板在渲染时将 props 传递给插槽出口：
vue-html


{{ receivedProps.text }} {{ receivedProps.count }}


vue-html


<slot
text="hello"
:count="1"
/>

使用单个默认插槽和使用具名插槽时，接收插槽 props 的方式略有不同。上面的示例通过在 ChildComponent 标签上直接使用 v-slot，用单个默认插槽接收 props。
!展示作用域插槽的图示：子组件将数据传回父级提供的插槽内容
在演练场中尝试一下
在演练场中尝试一下
子组件传入插槽的 props 作为了 v-slot 指令的值，可以在插槽内的表达式中访问。
你可以将作用域插槽类比为一个传入子组件的函数。子组件会将相应的 props 作为参数传给它：
js
ChildComponent({
// 将默认插槽以函数形式传递
default: (receivedProps) => {
return ${receivedProps.text} ${receivedProps.count}
}
})
function ChildComponent(slots) {
// 带着 props 调用插槽函数！
return slots.default({ text: 'hello', count: 1 })
}

实际上，这已经和作用域插槽的最终代码编译结果、以及手动编写渲染函数时使用作用域插槽的方式非常类似了。
注意 v-slot="receivedProps" 与插槽函数签名的匹配。和函数参数类似，我们也可以在 v-slot 中使用解构：
vue-html

{{ text }} {{ count }}


### 具名作用域插槽 
具名作用域插槽的工作方式也是类似的——插槽 props 可以作为 v-slot 指令的值被访问到：v-slot:name="receivedProps"。使用缩写时是这样：
vue-html


{{ headerProps }}


{{ defaultProps }}


{{ footerProps }}



向具名插槽中传入 props：
vue-html


注意插槽上的 name 是一个 Vue 特别保留的 attribute，不会作为 props 传递给插槽。因此最终 headerProps 的结果是 { message: 'hello' }。
如果你同时使用了具名插槽与默认插槽，则需要为默认插槽使用显式的  标签。尝试直接为组件添加 v-slot 指令将导致编译错误。这是为了避免因默认插槽的 props 的作用域而困惑。举例：
vue-html
 template -->





vue-html


{{ message }}


{{ message }}



为默认插槽使用显式的  标签有助于更清晰地指出 message 属性在其他插槽中不可用：
vue-html



{{ message }}


Here's some contact info



### 高级列表组件示例 
你可能想问什么样的场景才适合用到作用域插槽，这里我们来看一个  组件的例子。它会渲染一个列表，并同时会封装一些加载远端数据的逻辑、使用数据进行列表渲染、或者是像分页或无限滚动这样更进阶的功能。然而我们希望它能够保留足够的灵活性，将对单个列表元素内容和样式的控制权留给使用它的父组件。我们期望的用法可能是这样的：
vue-html



{{ body }}
by {{ username }} | {{ likes }} likes




在  之中，我们可以多次渲染  并每次都提供不同的数据 (注意我们这里使用了 v-bind 来传递插槽的 props)：
vue-html






在演练场中尝试一下
在演练场中尝试一下
### 无渲染组件 
上面的  案例同时封装了可重用的逻辑 (数据获取、分页等) 和视图输出，但也将部分视图输出通过作用域插槽交给了消费者组件来管理。
如果我们将这个概念拓展一下，可以想象的是，一些组件可能只包括了逻辑而不需要自己渲染内容，视图输出通过作用域插槽全权交给了消费者组件。我们将这种类型的组件称为无渲染组件。
这里有一个无渲染组件的例子，一个封装了追踪当前鼠标位置逻辑的组件：
vue-html

Mouse is at: {{ x }}, {{ y }}


在演练场中尝试一下
在演练场中尝试一下
虽然这个模式很有趣，但大部分能用无渲染组件实现的功能都可以通过组合式 API 以另一种更高效的方式实现，并且还不会带来额外组件嵌套的开销。之后我们会在组合式函数一章中介绍如何更高效地实现追踪鼠标位置的功能。
尽管如此，作用域插槽在需要同时封装逻辑、组合视图界面时还是很有用，就像上面的  组件那样。