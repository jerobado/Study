# Graphics View Framework
- Graphics View provides a surface for managing and interacting with a large number of custom-made 2D graphical items, and a view widget for visualizing the items, with support for zooming and rotation.


## Concepts

### Scene
- `QGraphicsScene` provides the Graphics View scene.
- The scene serves as a container for `QGraphicsItem` objects. 
- Items are added to the scene by calling `QGraphicsScene::addItem()`.

    ```c++
    QGraphicsScene scene;
    QGraphicsRectItem *rect = scene.addRect(QRectF(0, 0, 100, 100));

    QGraphicsItem *item = scene.itemAt(50, 50, QTransform());
    ```

### View
- `QGraphicsView` provides the view widget, which visualizes the contents of a scene.
-  You can attach several views to the same scene, to provide several viewports into the same data set.
- The view receives input events from the keyboard and mouse, and translates these to scene events (converting the coordinates used to scene coordinates where appropriate), before sending the events to the visualized scene.

    ```c++
    QGraphicsScene scene;
    QGraphicsView view(&scene);
    view.show();
    ```

### Item
- `QGraphicsItem` is the base class for graphical items in a scene.




## References
- [Graphics View Framework](https://doc.qt.io/qt-6/graphicsview.html)