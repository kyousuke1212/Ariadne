# TypeScript 工具类型 
此页面仅列出了一些可能需要解释其使用方式的常用工具类型。有关导出类型的完整列表，请查看源代码。
## PropType\ 
用于在用运行时 props 声明时给一个 prop 标注更复杂的类型定义。
* 示例
ts
import type { PropType } from 'vue'
interface Book {
title: string
author: string
year: number
}
export default {
props: {
book: {
// 提供一个比 Object 更具体的类型
type: Object as PropType,
required: true
}
}
}

* 参考指南 - 为组件 props 标注类型
## MaybeRef\ 
* 仅在 3.3+ 版本中支持。
T | Ref 的别名。对于标注组合式函数的参数很有用。
## MaybeRefOrGetter\ 
* 仅在 3.3+ 版本中支持。
T | Ref | (() => T) 的别名。对于标注组合式函数的参数很有用。
## ExtractPropTypes\ 
从运行时的 props 选项对象中提取 props 类型。提取到的类型是面向内部的，也就是说组件接收到的是解析后的 props。这意味着 boolean 类型的 props 和带有默认值的 props 总是一个定义的值，即使它们不是必需的。
要提取面向外部的 props，即父组件允许传递的 props，请使用 ExtractPublicPropTypes。
* 示例
ts
const propsOptions = {
foo: String,
bar: Boolean,
baz: {
type: Number,
required: true
},
qux: {
type: Number,
default: 1
}
} as const
type Props = ExtractPropTypes
// {
//   foo?: string,
//   bar: boolean,
//   baz: number,
//   qux: number
// }

## ExtractPublicPropTypes\ 
* 仅在 3.3+ 版本中支持。
从运行时的 props 选项对象中提取 prop。提取的类型是面向外部的，即父组件允许传递的 props。
* 示例
ts
const propsOptions = {
foo: String,
bar: Boolean,
baz: {
type: Number,
required: true
},
qux: {
type: Number,
default: 1
}
} as const
type Props = ExtractPublicPropTypes
// {
//   foo?: string,
//   bar?: boolean,
//   baz: number,
//   qux?: number
// }

## ComponentCustomProperties 
用于增强组件实例类型以支持自定义全局属性。
* 示例
ts
import axios from 'axios'
declare module 'vue' {
interface ComponentCustomProperties {
$http: typeof axios
$translate: (key: string) => string
}
}

类型扩展必须被放置在一个模块 .ts 或 .d.ts 文件中。查看类型扩展指南了解更多细节。
* 参考指南 - 扩展全局属性
## ComponentCustomOptions 
用来扩展组件选项类型以支持自定义选项。
* 示例
ts
import { Route } from 'vue-router'
declare module 'vue' {
interface ComponentCustomOptions {
beforeRouteEnter?(to: any, from: any, next: () => void): void
}
}

类型扩展必须被放置在一个模块 .ts 或 .d.ts 文件中。查看类型扩展指南了解更多细节。
* 参考指南 - 扩展自定义选项
## ComponentCustomProps 
用于扩展全局可用的 TSX props，以便在 TSX 元素上使用没有在组件选项上定义过的 props。
* 示例
ts
declare module 'vue' {
interface ComponentCustomProps {
hello?: string
}
}
export {}

tsx
// 现在即使没有在组件选项上定义过 hello 这个 prop 也依然能通过类型检查了


类型扩展必须被放置在一个模块 .ts 或 .d.ts 文件中。查看类型扩展指南了解更多细节。
## CSSProperties 
用于扩展在样式属性绑定上允许的值的类型。
* 示例
允许任意自定义 CSS 属性：
ts
declare module 'vue' {
interface CSSProperties {
[key: --${string}]: string
}
}

tsx


html


类型增强必须被放置在一个模块 .ts 或 .d.ts 文件中。查看类型增强指南了解更多细节。
单文件组件  标签支持通过 v-bind CSS 函数来链接 CSS 值与组件状态。这允许在没有类型扩展的情况下自定义属性。
* CSS 中的 v-bind()