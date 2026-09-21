# 组合式 API：辅助 
## useAttrs() 
从 Setup 上下文中返回 attrs 对象，其中包含当前组件的透传 attributes。这是用于  中的，因为在  中无法获取 setup 上下文对象。
* 类型
ts
function useAttrs(): Record

## useSlots() 
从 Setup 上下文中返回 slots 对象，其中包含父组件传递的插槽。这些插槽为可调用的函数，返回虚拟 DOM 节点。这是用于  中的，因为在  中无法获取 setup 上下文对象。
如果使用 TypeScript，建议优先使用 defineSlots()。
* 类型
ts
function useSlots(): Record VNode[]>

## useModel() 
这是驱动 defineModel() 的底层辅助函数。如果使用 ，应当优先使用 defineModel()。
* 仅在 3.4+ 版本中可用
* 类型
ts
function useModel(
props: Record,
key: string,
options?: DefineModelOptions
): ModelRef
type DefineModelOptions = {
get?: (v: T) => any
set?: (v: T) => any
}
type ModelRef = Ref & [
ModelRef,
Record
]

* 示例
js
export default {
props: ['count'],
emits: ['update:count'],
setup(props) {
const msg = useModel(props, 'count')
msg.value = 1
}
}

* 详细信息
useModel() 可以用于非单文件组件，例如在使用原始的 setup() 函数时。它预期的第一个参数是 props 对象，第二个参数是 model 名称。可选的第三个参数可以用于为生成的 model ref 声明自定义的 getter 和 setter。请注意，与 defineModel() 不同，你需要自己声明 props 和 emits。
## useTemplateRef()  
返回一个浅层 ref，其值将与模板中的具有匹配 ref attribute 的元素或组件同步。
* 类型
ts
function useTemplateRef(key: string): Readonly>

* 示例
vue

import { useTemplateRef, onMounted } from 'vue'
const inputRef = useTemplateRef('input')
onMounted(() => {
inputRef.value.focus()
})





* 参考
* 指南 - 模板引用
* 指南 - 为模板引用标注类型&#x20;
* 指南 - 为组件模板引用标注类型&#x20;
## useId()  
用于为无障碍属性或表单元素生成每个应用内唯一的 ID。
* 类型
ts
function useId(): string

* 示例
vue

import { useId } from 'vue'
const id = useId()



Name:




* 详细信息
useId() 生成的每个 ID 在每个应用内都是唯一的。它可以用于为表单元素和无障碍属性生成 ID。在同一个组件中多次调用会生成不同的 ID；同一个组件的多个实例调用 useId() 也会生成不同的 ID。
useId() 生成的 ID 在服务器端和客户端渲染之间是稳定的，因此可以安全地在 SSR 应用中使用，不会导致激活不匹配。
如果同一页面上有多个 Vue 应用实例，可以通过 app.config.idPrefix 为每个应用提供一个 ID 前缀，以避免 ID 冲突。
useId() 不应在 computed() 属性内部调用，因为这可能导致实例冲突。相反，应在 computed() 外部声明 ID，并在计算函数内部引用它。