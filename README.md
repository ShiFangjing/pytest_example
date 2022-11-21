# pytest_example
****2022/11/21****

fixture的作用范围示例：
- function：默认值，函数或方法级别被调用，当函数执行结束后，fixture则被销毁
- class：类级别调用一次，当类中的最后一个测试函数执行结束后，fixture则被销毁
- module：模块级别的（每一个.py文件）调用一次，当模块中最后一个测试函数执行结束后，fixture则被销毁
- package：包（一个文件夹下的.py文件）级别调用一次，当包最后一个测试函数执行结束后，fixture则被销毁
- session：一个会话调用一次（可理解为整个项目调用一次）多个包调用一次，当多个包最后一个测试函数结束后，fixture则被销毁

谨记：fixture是在测试首次请求时创建的，并基于它们的作用域被销毁。（Fixtures are created when first requested by a test, and are destroyed based on their scope。）
所以被fixture修饰的函数并不会主动被执行，会在调用的时候被第一次执行，scope控制的只是fixture的销毁时间。

建议：用参数化方式使用fixture
