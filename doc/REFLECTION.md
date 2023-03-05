# Reflection for Study Bird 551 Project
**Topic: **Billboard Top100 Hot🔥🔥Songs🔥🔥Analysis
**Group Members: **Nyx, Tia, Yuhong


## Implemented  
1. **The objectives and directions:** For the hottest songs, represented by Billboard top100 chart, we wanted to understand their characteristics and also how they have changed over the years.
2. **The indicators represented the characteristics and their calibers:** There are three objects of characteristics, each aspects contain several dimensions. ([README.md](https://github.com/petitmi/Study-Bird-551/readme.md))

3. **The various visualization of characteristics:**
   - Basic bar charts, line charts, pie chars
   - Complex box plots, wordcloud plots, stack plots
   - Compound multi-axies and multi-dimension plots
4. **User interaction and structure**
 <table>
    <thead>
        <tr>
            <th colspan="2"  text-align= "left">Title</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Side bar: Tab selection</td>
            <td>Range selection</td>
        </tr>
        <tr>
            <td>Main page container:  Iframe plots</td>
        </tr>
        <tr>
            <td colspan="2">Footer</td>
        </tr>
    </tbody>
</table>

## Unimplemented
1. Each analysis object selected the dimensions that were considered most important and did not cover more and more complete dimensions. Improvements could be made by adding selection components.
2. More detailed features were not implemented: for example, the analysis of lyrics displayed by search keywords.
<!-- 
【实现了什么】
1. 想要分析的思路各个维度都实现了：
（1）对于每年最火的音乐，想了解整体有什么特点，还想了解特点逐年有什么变化。
（2）特点主要基于三个方面：歌曲音乐性、文学性和歌手。每个方面分别有三个维度
（3）歌曲的音乐性：音乐scale， 节奏律动，氛围。
（4）歌曲的文学性：歌词物理长度，情感，主题
（5）歌手分析：歌手的流行程度、资历（出道时长）、敬业/活跃程度（专辑数量）
2. 想要实现多种可视化图表，包括
（1）基础的柱状图、折线图、扇形图
（2）复杂的箱线图、词云图、堆积图
（3）组合的多轴多维图等
3. 网页的交互效果
（1）layout、标题、页面、页尾、侧边栏
（2）组件：菜单、rangeselection
（3）核心的可视化图：Iframe

【未实现】
1. 每个分析主题选取了认为最重要的维度，没有覆盖更多更全的维度。改善方法是可以增加选择组件。
2. 更细节的功能未能实现：比如通过搜索关键词来展示歌词的分析。 -->

## Other reflections:

1. **Analysis ideas** 
- The process of determining the analysis theme do get a quick agreement, each member has a strong interest in music analysis, and actively communicate out a very specific application scenario. 
- Realization of the scenario: When thinking about what specifically can be done also need to combine what data can be available, sometimes get caught in the confusion. Finally, I found that starting from thinking about how to do it specifically to thinking about what I want to analyze first will have better results and can achieve what I want more effectively.
2. **Data processing**
- Data sources involved in crawlers, interfaces, but fortunately started to do early, in the middle of the problem of restricted access to have time to deal with. For example, the interface document shows the existence of a field, but not actually; or the interface can only be accessed 70 times a day, but we actually call 1000 times.
- Data cleaning costs a lot, fortunately for learning pandas. but still need to query a lot of information. 70% of the time spent on cleaning. In the future, as much as possible to assess the reliability of data in advance 
- Debug: visualization of the main application altair, more familiar, but because plotly + altair + python there are version differences, halfway through the encounter some function failure, such as html. 
- Existing modules, resources are not enough to achieve the goal: some want to achieve the fancy chart, altair can not achieve, together with a meeting to discuss to determine a method.
3. **Aesthetics and consistency**  
The earliest color series was set first, and we continued to communicate during the process
5. **Collaboration**  
- In addition to each person being responsible for an analysis page, other tasks were distributed almost equally, such as overall layout code, deployment code, etc. In order to take advantage of teamwork, a person to complete the framework, in the details of the difficulties encountered or need to discuss are actively cooperate with the discussion program and help debug, etc., such as the sidebar bugs.

<!-- 
1. 分析思路：（1）分析主题的确定过程做得到快速达成一致，每位成员都对音乐分析有浓厚的兴趣，并积极沟通出了非常具体的应用场景。（2）实现方案：在思考具体能做什么的时候还需要结合能有什么数据，有时候会陷入混乱中。最后发现从想具体怎么做开始转变为先思考想要分析什么，会有更好的效果，能更有效的达到自己想要的。
2. 数据处理方面：（1）数据源涉及爬虫、接口，还好提早开始做，中间遇到访问受限的问题有时间去处理。比如接口文档显示存在某字段，但实际没有；或者接口一天只能访问70次，但我们实际调用1000次（2）数据清洗成本大，还好对学过pandas。但是仍然需要查询很多资料。70%的时间用在了清洗。以后尽可能多提前评估数据可靠性（3）debug：可视化主要应用altair，较为熟悉，但因为plotly+altair+python存在版本差异，中途遇到一些函数失效，比如html.Img，最后发现需要写底层的实现代码。（4）现有的模块、资源不足实现目标：一些想实现的fancy图，altair无法实现，一起开会讨论确定了一个方法。
3. 美观与一致性方面：最早先定下色彩系列，过程中持续沟通
4. 协作方面：每人除了负责一个分析页面外，还近乎平均分配了其他工作，比如整体布局代码、部署代码等。为了发挥团队合作的优势，一个人完成框架，在细节方面遇到困难或需要讨论都积极配合讨论方案与帮助debug等，比如sidebar的bug。 -->
