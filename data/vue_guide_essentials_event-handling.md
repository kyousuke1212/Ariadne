# 事件处理 
## 监听事件 
我们可以使用 v-on 指令 (简写为 @) 来监听 DOM 事件，并在事件触发时执行对应的 JavaScript。用法：v-on:click="handler" 或 @click="handler"。
事件处理器 (handler) 的值可以是：
1. 内联事件处理器：事件被触发时执行的内联 JavaScript 语句 (与 onclick 类似)。
2. 方法事件处理器：一个指向组件上定义的方法的属性名或是路径。
## 内联事件处理器 
内联事件处理器通常用于简单场景，例如：
js
const count = ref(0)

js
data() {
return {
count: 0
}
}

vue-html
Add 1
Count is: {{ count }}

在演练场中尝试一下
在演练场中尝试一下
## 方法事件处理器 
随着事件处理器的逻辑变得愈发复杂，内联代码方式变得不够灵活。因此 v-on 也可以接受一个方法名或对某个方法的调用。
举例来说：
js
const name = ref('Vue.js')
function greet(event) {
alert(Hello ${name.value}!)
// event 是 DOM 原生事件
if (event) {
alert(event.target.tagName)
}
}

js
data() {
return {
name: 'Vue.js'
}
},
methods: {
greet(event) {
// 方法中的 this 指向当前活跃的组件实例
alert(Hello ${this.name}!)
// event 是 DOM 原生事件
if (event) {
alert(event.target.tagName)
}
}
}

vue-html

Greet

在演练场中尝试一下
在演练场中尝试一下
方法事件处理器会自动接收原生 DOM 事件并触发执行。在上面的例子中，我们能够通过被触发事件的 event.target 访问到该 DOM 元素。
你也可以看看为事件处理器标注类型这一章了解更多。
你也可以看看为事件处理器标注类型这一章了解更多。
### 方法与内联事件判断 
模板编译器会通过检查 v-on 的值是否是合法的 JavaScript 标识符或属性访问路径来断定是何种形式的事件处理器。举例来说，foo、foo.bar 和 foo['bar'] 会被视为方法事件处理器，而 foo() 和 count++ 会被视为内联事件处理器。
## 在内联处理器中调用方法 
除了直接绑定方法名，你还可以在内联事件处理器中调用方法。这允许我们向方法传入自定义参数以代替原生事件：
js
function say(message) {
alert(message)
}

js
methods: {
say(message) {
alert(message)
}
}

vue-html
Say hello
Say bye

在演练场中尝试一下
在演练场中尝试一下
## 在内联事件处理器中访问事件参数 
有时我们需要在内联事件处理器中访问原生 DOM 事件。你可以向该处理器方法传入一个特殊的 $event 变量，或者使用内联箭头函数：
vue-html


Submit


 warn('Form cannot be submitted yet.', event)">
Submit


js
function warn(message, event) {
// 这里可以访问原生事件
if (event) {
event.preventDefault()
}
alert(message)
}

js
methods: {
warn(message, event) {
// 这里可以访问 DOM 原生事件
if (event) {
event.preventDefault()
}
alert(message)
}
}

## 事件修饰符 
在处理事件时调用 event.preventDefault() 或 event.stopPropagation() 是很常见的。尽管我们可以直接在方法内调用，但如果方法能更专注于数据逻辑而不用去处理 DOM 事件的细节会更好。
为解决这一问题，Vue 为 v-on 提供了事件修饰符。修饰符是用 . 表示的指令后缀，包含以下这些：
* .stop
* .prevent
* .self
* .capture
* .once
* .passive
vue-html










...

使用修饰符时需要注意调用顺序，因为相关代码是以相同的顺序生成的。因此使用 @click.prevent.self 会阻止元素及其子元素的所有点击事件的默认行为，而 @click.self.prevent 则只会阻止对元素本身的点击事件的默认行为。
.capture、.once 和 .passive 修饰符与原生 addEventListener 事件相对应：
vue-html


...




...

.passive 修饰符一般用于触摸事件的监听器，可以用来改善移动端设备的滚屏性能。
请勿同时使用 .passive 和 .prevent，因为 .passive 已经向浏览器表明了你*不想*阻止事件的默认行为。如果你这么做了，则 .prevent 会被忽略，并且浏览器会抛出警告。
## 按键修饰符 
在监听键盘事件时，我们经常需要检查特定的按键。Vue 允许在 v-on 或 @ 监听按键事件时添加按键修饰符。
vue-html



你可以直接使用 KeyboardEvent.key 暴露的按键名称作为修饰符，但需要转为 kebab-case 形式。
vue-html


在上面的例子中，仅会在 $event.key 为 'PageDown' 时调用事件处理。
### 按键别名 
Vue 为一些常用的按键提供了别名：
* .enter
* .tab
* .delete (捕获“Delete”和“Backspace”两个按键)
* .esc
* .space
* .up
* .down
* .left
* .right
### 系统按键修饰符 
你可以使用以下系统按键修饰符来触发鼠标或键盘事件监听器，只有当按键被按下时才会触发。
* .ctrl
* .alt
* .shift
* .meta
在 Mac 键盘上，meta 是 Command 键 (⌘)。在 Windows 键盘上，meta 键是 Windows 键 (⊞)。在 Sun 微机系统键盘上，meta 是钻石键 (◆)。在某些键盘上，特别是 MIT 和 Lisp 机器的键盘及其后代版本的键盘，如 Knight 键盘，space-cadet 键盘，meta 都被标记为“META”。在 Symbolics 键盘上，meta 也被标识为“META”或“Meta”。
举例来说：
vue-html



Do something

请注意，系统按键修饰符和常规按键不同。与 keyup 事件一起使用时，该按键必须在事件发出时处于按下状态。换句话说，keyup.ctrl 只会在你仍然按住 ctrl 但松开了另一个键时被触发。若你单独松开 ctrl 键将不会触发。
### .exact 修饰符 
.exact 修饰符允许精确控制触发事件所需的系统修饰符的组合。
vue-html

A

A

A

## 鼠标按键修饰符 
* .left
* .right
* .middle
这些修饰符将处理程序限定为由特定鼠标按键触发的事件。
但请注意，.left，.right 和 .middle 这些修饰符名称是基于常见的右手用鼠标布局设定的，但实际上它们分别指代设备事件触发器的“主”、“次”，“辅助”，而非实际的物理按键。因此，对于左手用鼠标布局而言，“主”按键在物理上可能是右边的按键，但却会触发 .left 修饰符对应的处理程序。又或者，触控板可能通过单指点击触发 .left 处理程序，通过双指点击触发 .right 处理程序，通过三指点击触发 .middle 处理程序。同样，产生“鼠标”事件的其他设备和事件源，也可能具有与“左”，“右”完全无关的触发模式。