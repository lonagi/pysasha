```python
from jupyterthemes import jtplot
jtplot.style(theme='chesterish')
# set "context" (paper, notebook, talk, poster)
jtplot.style(context='talk', fscale=1.4, spines=True, gridlines='--')
jtplot.style(ticks=True, grid=True, figsize=(6, 4.5))
#jtplot.reset()
```

$$ {{145}\over{99}} = {{1+\sqrt[3]{{29+3\sqrt{93}}\over{2}} +\sqrt[3]{{29-3\sqrt{93}}\over{2}} }\over{3} } $$


```python
import time
s = []
for i in range(1000,2000):
    start_time = time.time()
    #SieveofEratosthenes(i)
    #lis1(i)
    end_time = (time.time() - start_time)
    s.append(end_time)
    #print("--- %s seconds ---" % end_time)
print(s)
```


```python

```


```python

```


```python
from ipywidgets import interact
import ipywidgets as widgets
def f(x):
    return x**2
# Generate a slider 
interact(f, x=10,);
```


```python
import qgrid
import pandas as pd

df =pd.DataFrame([[j for j in range(100)] for i in range(100)])
#df.to_html()
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>90</th>
      <th>91</th>
      <th>92</th>
      <th>93</th>
      <th>94</th>
      <th>95</th>
      <th>96</th>
      <th>97</th>
      <th>98</th>
      <th>99</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>...</td>
      <td>90</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
      <td>94</td>
      <td>95</td>
      <td>96</td>
      <td>97</td>
      <td>98</td>
      <td>99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>...</td>
      <td>90</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
      <td>94</td>
      <td>95</td>
      <td>96</td>
      <td>97</td>
      <td>98</td>
      <td>99</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>...</td>
      <td>90</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
      <td>94</td>
      <td>95</td>
      <td>96</td>
      <td>97</td>
      <td>98</td>
      <td>99</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>...</td>
      <td>90</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
      <td>94</td>
      <td>95</td>
      <td>96</td>
      <td>97</td>
      <td>98</td>
      <td>99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>...</td>
      <td>90</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
      <td>94</td>
      <td>95</td>
      <td>96</td>
      <td>97</td>
      <td>98</td>
      <td>99</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>...</td>
      <td>90</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
      <td>94</td>
      <td>95</td>
      <td>96</td>
      <td>97</td>
      <td>98</td>
      <td>99</td>
    </tr>
    <tr>
      <th>96</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>...</td>
      <td>90</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
      <td>94</td>
      <td>95</td>
      <td>96</td>
      <td>97</td>
      <td>98</td>
      <td>99</td>
    </tr>
    <tr>
      <th>97</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>...</td>
      <td>90</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
      <td>94</td>
      <td>95</td>
      <td>96</td>
      <td>97</td>
      <td>98</td>
      <td>99</td>
    </tr>
    <tr>
      <th>98</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>...</td>
      <td>90</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
      <td>94</td>
      <td>95</td>
      <td>96</td>
      <td>97</td>
      <td>98</td>
      <td>99</td>
    </tr>
    <tr>
      <th>99</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>...</td>
      <td>90</td>
      <td>91</td>
      <td>92</td>
      <td>93</td>
      <td>94</td>
      <td>95</td>
      <td>96</td>
      <td>97</td>
      <td>98</td>
      <td>99</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 100 columns</p>
</div>




```python

```
