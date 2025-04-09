# SymPy 绘图实验报告

## 一、实验信息

- 小组名称：
- 成员：
- 实验日期：

---

## 二、实验目的

- 熟悉SymPy的plot、plot_implicit、和plot3d_parametric_surface函数；
- 掌握曲线、隐函数和参数曲面的绘制方法。

---

## 三、实验内容与方法

分别说明三个问题的具体绘图方法和使用的函数接口。
以下是三个问题的具体绘图方法和使用的函数接口说明：

---

### **问题 1：绘制函数 `cos(tan(pi*x))` 的图像**
#### 方法：
1. 使用 `sympy.plotting.plot` 函数绘制函数图像。
2. 定义符号变量 `x` 和表达式 `cos(tan(pi*x))`。
3. 设置绘图范围为 `x ∈ [-1, 1]`。
4. 添加坐标轴标签 `xlabel='x'` 和 `ylabel='cos(tan(pi*x))'`，以及标题 `title='Function Plot'`。

#### 函数接口：
```python
plot(expr, (var, start, end), xlabel='x', ylabel='y', title='Title', show=True)
```
- `expr`：要绘制的表达式。
- `(var, start, end)`：变量及其范围。
- `xlabel` 和 `ylabel`：坐标轴标签。
- `title`：图像标题。
- `show`：是否显示图像，默认为 `True`。

---

### **问题 2：绘制隐函数 `e^y + cos(x)/x + y = 0` 的图像**
#### 方法：
1. 使用 `sympy.plotting.plot_implicit` 函数绘制隐函数图像。
2. 定义符号变量 `x` 和 `y`。
3. 定义隐函数表达式 `e^y + cos(x)/x + y = 0`。
4. 设置绘图区间为 `x ∈ [-10, 10]` 和 `y ∈ [-10, 10]`，避免 `x=0` 的除零错误。
5. 添加坐标轴标签 `xlabel='x'` 和 `ylabel='y'`，以及标题 `title='Implicit Function Plot'`。
6. 设置 `points=500` 参数以提高图像质量。

#### 函数接口：
```python
plot_implicit(expr, (x, x_start, x_end), (y, y_start, y_end), xlabel='x', ylabel='y', title='Title', points=500, show=True)
```
- `expr`：隐函数表达式，通常使用 `sp.Eq()` 定义。
- `(x, x_start, x_end)` 和 `(y, y_start, y_end)`：变量及其范围。
- `xlabel` 和 `ylabel`：坐标轴标签。
- `title`：图像标题。
- `points`：采样点数量，默认值为 300。
- `show`：是否显示图像，默认为 `True`。

---

### **问题 3：绘制三维参数曲面**
#### 方法：
1. 使用 `sympy.plotting.plot3d_parametric_surface` 函数绘制三维参数曲面。
2. 定义符号变量 `s` 和 `t`。
3. 定义参数方程：
   - `x = exp(-s) * cos(t)`
   - `y = exp(-s) * sin(t)`
   - `z = t`
4. 设置参数范围为 `s ∈ [0, 8]` 和 `t ∈ [0, 5*pi]`。
5. 添加坐标轴标签 `xlabel='x'`、`ylabel='y'` 和 `zlabel='z'`，以及标题 `title='3D Parametric Surface'`。

#### 函数接口：
```python
plot3d_parametric_surface(x_expr, y_expr, z_expr, (u, u_start, u_end), (v, v_start, v_end), xlabel='x', ylabel='y', zlabel='z', title='Title', show=True)
```
- `x_expr`、`y_expr` 和 `z_expr`：参数方程的表达式。
- `(u, u_start, u_end)` 和 `(v, v_start, v_end)`：参数及其范围。
- `xlabel`、`ylabel` 和 `zlabel`：坐标轴标签。
- `title`：图像标题。
- `show`：是否显示图像，默认为 `True`。

---

### 总结
- **问题 1** 使用 `plot` 函数绘制一维函数图像。
- **问题 2** 使用 `plot_implicit` 函数绘制隐函数图像。
- **问题 3** 使用 `plot3d_parametric_surface` 函数绘制三维参数曲面。


---

## 四、实验结果与分析

### 问题1: 函数曲线 $\cos(\tan(\pi x))$ 绘制结果

![problem1_plot](https://github.com/user-attachments/assets/1efd607c-e964-4890-bce3-6c8f7d055452)

绘制结果特点：
### 周期性：

函数 $\cos(\tan(\pi x))$ 是由 $\cos$ 和 $\tan$ 组合而成。
$\tan(\pi x)$ 在 $x = \pm 0.5, \pm 1.5, \pm 2.5, \dots$ 处会趋于无穷大，因此 $\cos(\tan(\pi x))$ 在这些点附近会表现出快速振荡。
### 振荡性：

$\cos$ 函数的值域为 $[-1, 1]$，因此 $\cos(\tan(\pi x))$ 的值域也限制在 $[-1, 1]$。
由于 $\tan(\pi x)$ 的非线性增长，$\cos(\tan(\pi x))$ 的振荡频率会随着 $x$ 的变化变得不规则。
### 对称性：

$\tan(\pi x)$ 是奇函数，而 $\cos$ 是偶函数，因此 $\cos(\tan(\pi x))$ 是偶函数，即关于 $y$ 轴对称。
### 间断性：

$\tan(\pi x)$ 在 $x = \pm 0.5, \pm 1.5, \dots$ 处无定义，因此 $\cos(\tan(\pi x))$ 在这些点附近会出现间断。
### 简要分析：
在绘制区间 $x \in [-1, 1]$ 内，函数 $\cos(\tan(\pi x))$ 会在 $x = -0.5$ 和 $x = 0.5$ 附近表现出剧烈的振荡。
曲线在 $x = 0$ 附近较为平滑，因为 $\tan(\pi x)$ 在 $x = 0$ 附近变化较慢。
由于 $\tan(\pi x)$ 的间断性，曲线在 $x = \pm 0.5$ 附近会出现不连续的跳跃。

### 问题2: 隐函数曲线 $e^y + \frac{\cos x}{x} + y = 0$ 绘制结果

*(插入图片或截图并简要分析隐函数曲线特点)*

### 问题3: 参数曲面绘制结果

*(插入图片或截图并简要分析三维曲面的特点)*

---

## 五、实验总结与讨论

- 通过本实验你掌握了哪些绘图技巧？
- 实验中你遇到了哪些问题？如何解决？
- 你对SymPy的绘图功能有什么建议或意见？

---

## 六、参考文献

- SymPy官方文档：https://docs.sympy.org/latest/modules/plotting.html
