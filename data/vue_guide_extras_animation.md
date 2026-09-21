# 动画技巧 
Vue 提供了  和  组件来处理元素进入、离开和列表顺序变化的过渡效果。但除此之外，还有许多其他制作网页动画的方式在 Vue 应用中也适用。这里我们会探讨一些额外的技巧。
## 基于 CSS class 的动画 
对于那些不是正在进入或离开 DOM 的元素，我们可以通过给它们动态添加 CSS class 来触发动画：
js
const disabled = ref(false)
function warnDisabled() {
disabled.value = true
setTimeout(() => {
disabled.value = false
}, 1500)
}

js
export default {
data() {
return {
disabled: false
}
},
methods: {
warnDisabled() {
this.disabled = true
setTimeout(() => {
this.disabled = false
}, 1500)
}
}
}

vue-html

Click me
This feature is disabled!


css
.shake {
animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
transform: translate3d(0, 0, 0);
}
@keyframes shake {
10%,
90% {
transform: translate3d(-1px, 0, 0);
}
20%,
80% {
transform: translate3d(2px, 0, 0);
}
30%,
50%,
70% {
transform: translate3d(-4px, 0, 0);
}
40%,
60% {
transform: translate3d(4px, 0, 0);
}
}

## 状态驱动的动画 
有些过渡效果可以通过动态插值来实现，比如在交互时动态地给元素绑定样式。看下面这个例子：
js
const x = ref(0)
function onMousemove(e) {
x.value = e.clientX
}

js
export default {
data() {
return {
x: 0
}
},
methods: {
onMousemove(e) {
this.x = e.clientX
}
}
}

vue-html
<div
@mousemove="onMousemove"
:style="{ backgroundColor: hsl(${x}, 80%, 50%) }"
class="movearea"
>
Move your mouse across this div...
x: {{ x }}


css
.movearea {
transition: 0.3s background-color ease;
}

除了颜色外，你还可以使用样式绑定 CSS transform、宽度或高度。你甚至可以通过运用弹性物理模拟为 SVG 添加动画，毕竟它们也只是 attribute 的数据绑定：
## 基于侦听器的动画 
通过发挥一些创意，我们可以基于一些数字状态，配合侦听器给任何东西加上动画。例如，我们可以将数字本身变成动画：
js
import { ref, reactive, watch } from 'vue'
import gsap from 'gsap'
const number = ref(0)
const tweened = reactive({
number: 0
})
// 注意：对于大于 Number.MAX_SAFE_INTEGER (9007199254740991) 的输入值，
// 由于 JavaScript 数字精度的限制，结果可能不准确。
watch(number, (n) => {
gsap.to(tweened, { duration: 0.5, number: Number(n) || 0 })
})

vue-html
Type a number: 
{{ tweened.number.toFixed(0) }}

js
import gsap from 'gsap'
export default {
data() {
return {
number: 0,
tweened: 0
}
},
// 注意：对于大于 Number.MAX_SAFE_INTEGER (9007199254740991) 的输入值，
// 由于 JavaScript 数字精度的限制，结果可能不准确。
watch: {
number(n) {
gsap.to(this, { duration: 0.5, tweened: Number(n) || 0 })
}
}
}

vue-html
Type a number: 
{{ tweened.toFixed(0) }}

在演练场中尝试一下
在演练场中尝试一下