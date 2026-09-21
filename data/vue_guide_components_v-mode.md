# 组件 v-model 
## 基本用法 
v-model 可以在组件上使用以实现双向绑定。
从 Vue 3.4 开始，推荐的实现方式是使用 defineModel() 宏：
vue [Child.vue]

const model = defineModel()
function update() {
model.value++
}


Parent bound v-model is: {{ model }}
Increment


父组件可以用 v-model 绑定一个值：
vue-html [Parent.vue]


defineModel() 返回的值是一个 ref。它可以像其他 ref 一样被访问以及修改，不过它能起到在父组件和当前变量之间的双向绑定的作用：
* 它的 .value 和父组件的 v-model 的值同步；
* 当它被子组件变更了，会触发父组件绑定的值一起更新。
这意味着你也可以用 v-model 把这个 ref 绑定到一个原生 input 元素上，在提供相同的 v-model 用法的同时轻松包装原生 input 元素：
vue

const model = defineModel()





演练场示例
### 底层机制 
defineModel 是一个便利宏。编译器将其展开为以下内容：
* 一个名为 modelValue 的 prop，本地 ref 的值与其同步；
* 一个名为 update:modelValue 的事件，当本地 ref 的值发生变更时触发。
在 3.4 版本之前，你一般会按照如下的方式来实现上述相同的子组件：
vue [Child.vue]

const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])


<input
:value="props.modelValue"
@input="emit('update:modelValue', $event.target.value)"
/>


然后，父组件中的 v-model="foo" 将被编译为：
vue-html [Parent.vue]
<Child
:modelValue="foo"
@update:modelValue="$event => (foo = $event)"
/>

如你所见，这显得冗长得多。然而，这样写有助于理解其底层机制。
因为 defineModel 声明了一个 prop，你可以通过给 defineModel 传递选项，来声明底层 prop 的选项：
js
// 使 v-model 必填
const model = defineModel({ required: true })
// 提供一个默认值
const model = defineModel({ default: 0 })

如果为 defineModel prop 设置了一个 default 值且父组件没有为该 prop 提供任何值，会导致父组件与子组件之间不同步。在下面的示例中，父组件的 myRef 是 undefined，而子组件的 model 是 1：
vue [Child.vue]

const model = defineModel({ default: 1 })


vue [Parent.vue]

const myRef = ref()





首先让我们回忆一下 v-model 在原生元素上的用法：
vue-html


在代码背后，模板编译器会对 v-model 进行更冗长的等价展开。因此上面的代码其实等价于下面这段：
vue-html
<input
:value="searchText"
@input="searchText = $event.target.value"
/>

而当使用在一个组件上时，v-model 会被展开为如下的形式：
vue-html
<CustomInput
:model-value="searchText"
@update:model-value="newValue => searchText = newValue"
/>

要让这个例子实际工作起来， 组件内部需要做两件事：
1. 将内部原生  元素的 value attribute 绑定到 modelValue prop
2. 当原生的 input 事件触发时，触发一个携带了新值的 update:modelValue 自定义事件
这里是相应的代码：
vue [CustomInput.vue]

export default {
props: ['modelValue'],
emits: ['update:modelValue']
}


<input
:value="modelValue"
@input="$emit('update:modelValue', $event.target.value)"
/>


现在 v-model 可以在这个组件上正常工作了：
vue-html


在演练场中尝试一下
另一种在组件内实现 v-model 的方式是使用一个可写的，同时具有 getter 和 setter 的 computed 属性。get 方法需返回 modelValue prop，而 set 方法需触发相应的事件：
vue [CustomInput.vue]

export default {
props: ['modelValue'],
emits: ['update:modelValue'],
computed: {
value: {
get() {
return this.modelValue
},
set(value) {
this.$emit('update:modelValue', value)
}
}
}
}





## v-model 的参数 
组件上的 v-model 也可以接受一个参数：
vue-html


在子组件中，我们可以通过将字符串作为第一个参数传递给 defineModel() 来支持相应的参数：
vue [MyComponent.vue]

const title = defineModel('title')





在演练场中尝试一下
如果需要额外的 prop 选项，应该在 model 名称之后传递：
js
const title = defineModel('title', { required: true })

vue [MyComponent.vue]

defineProps({
title: {
required: true
}
})
defineEmits(['update:title'])


<input
type="text"
:value="title"
@input="$emit('update:title', $event.target.value)"
/>


在演练场中尝试一下
在这种情况下，子组件应该使用 title prop 和 update:title 事件来更新父组件的值，而非默认的 modelValue prop 和 update:modelValue 事件：
vue [MyComponent.vue]

export default {
props: ['title'],
emits: ['update:title']
}


<input
type="text"
:value="title"
@input="$emit('update:title', $event.target.value)"
/>


在演练场中尝试一下
## 多个 v-model 绑定 
利用刚才在 v-model 的参数小节中学到的指定参数与事件名的技巧，我们可以在单个组件实例上创建多个 v-model 双向绑定。
组件上的每一个 v-model 都会同步不同的 prop，而无需额外的选项：
vue-html
<UserName
v-model:first-name="first"
v-model:last-name="last"
/>

vue

const firstName = defineModel('firstName')
const lastName = defineModel('lastName')






在演练场中尝试一下
vue

defineProps({
firstName: String,
lastName: String
})
defineEmits(['update:firstName', 'update:lastName'])


<input
type="text"
:value="firstName"
@input="$emit('update:firstName', $event.target.value)"
/>
<input
type="text"
:value="lastName"
@input="$emit('update:lastName', $event.target.value)"
/>


在演练场中尝试一下
vue

export default {
props: {
firstName: String,
lastName: String
},
emits: ['update:firstName', 'update:lastName']
}


<input
type="text"
:value="firstName"
@input="$emit('update:firstName', $event.target.value)"
/>
<input
type="text"
:value="lastName"
@input="$emit('update:lastName', $event.target.value)"
/>


在演练场中尝试一下
## 处理 v-model 修饰符 
在学习输入绑定时，我们知道了 v-model 有一些内置的修饰符，例如 .trim，.number 和 .lazy。在某些场景下，你可能想要一个自定义组件的 v-model 支持自定义的修饰符。
我们来创建一个自定义的修饰符 capitalize，它会自动将 v-model 绑定输入的字符串值第一个字母转为大写：
vue-html


通过像这样解构 defineModel() 的返回值，可以在子组件中访问添加到组件 v-model 的修饰符：
vue{4}

const [model, modifiers] = defineModel()
console.log(modifiers) // { capitalize: true }





为了能够基于修饰符选择性地调节值的读取和写入方式，我们可以给 defineModel() 传入 get 和 set 这两个选项。这两个选项在从模型引用中读取或设置值时会接收到当前的值，并且它们都应该返回一个经过处理的新值。下面是一个例子，展示了如何利用 set 选项来应用 capitalize (首字母大写) 修饰符：
vue{4-6}

const [model, modifiers] = defineModel({
set(value) {
if (modifiers.capitalize) {
return value.charAt(0).toUpperCase() + value.slice(1)
}
return value
}
})





在演练场中尝试一下
vue{11-13}

const props = defineProps({
modelValue: String,
modelModifiers: { default: () => ({}) }
})
const emit = defineEmits(['update:modelValue'])
function emitValue(e) {
let value = e.target.value
if (props.modelModifiers.capitalize) {
value = value.charAt(0).toUpperCase() + value.slice(1)
}
emit('update:modelValue', value)
}





在演练场中尝试一下
添加到组件 v-model 的修饰符将通过 modelModifiers prop 提供给组件。在下面的示例中，我们创建了一个包含 modelModifiers prop 的组件，该 prop 默认为空对象：
vue{11}

export default {
props: {
modelValue: String,
modelModifiers: {
default: () => ({})
}
},
emits: ['update:modelValue'],
created() {
console.log(this.modelModifiers) // { capitalize: true }
}
}


<input
type="text"
:value="modelValue"
@input="$emit('update:modelValue', $event.target.value)"
/>


请注意，该组件的 modelModifiers prop 包含 capitalize 且值为 true ——因为它是在 v-model.capitalize="myText" 这个 v-model 绑定上设置的。
现在我们已经为组件配置了 prop，我们可以检查 modelModifiers 对象的键并编写一个处理程序来更改抛出的值。在下面的代码中，每当  元素触发 input 事件时，我们都会将首字母大写。
vue{13-15}

export default {
props: {
modelValue: String,
modelModifiers: {
default: () => ({})
}
},
emits: ['update:modelValue'],
methods: {
emitValue(e) {
let value = e.target.value
if (this.modelModifiers.capitalize) {
value = value.charAt(0).toUpperCase() + value.slice(1)
}
this.$emit('update:modelValue', value)
}
}
}





在演练场中尝试一下
### 带参数的 v-model 修饰符 
对于又有参数又有修饰符的 v-model 绑定，生成的 prop 名将是 arg + "Modifiers"。举例来说：
vue-html


相应的声明应该是：
js
export default {
props: ['title', 'titleModifiers'],
emits: ['update:title'],
created() {
console.log(this.titleModifiers) // { capitalize: true }
}
}

这里是另一个例子，展示了如何在使用多个不同参数的 v-model 时使用修饰符：
vue-html
<UserName
v-model:first-name.capitalize="first"
v-model:last-name.uppercase="last"
/>

vue

const [firstName, firstNameModifiers] = defineModel('firstName')
const [lastName, lastNameModifiers] = defineModel('lastName')
console.log(firstNameModifiers) // { capitalize: true }
console.log(lastNameModifiers) // { uppercase: true }


vue{5,6,10,11}

const props = defineProps({
firstName: String,
lastName: String,
firstNameModifiers: { default: () => ({}) },
lastNameModifiers: { default: () => ({}) }
})
defineEmits(['update:firstName', 'update:lastName'])
console.log(props.firstNameModifiers) // { capitalize: true }
console.log(props.lastNameModifiers) // { uppercase: true }


vue{15,16}

export default {
props: {
firstName: String,
lastName: String,
firstNameModifiers: {
default: () => ({})
},
lastNameModifiers: {
default: () => ({})
}
},
emits: ['update:firstName', 'update:lastName'],
created() {
console.log(this.firstNameModifiers) // { capitalize: true }
console.log(this.lastNameModifiers) // { uppercase: true }
}
}

