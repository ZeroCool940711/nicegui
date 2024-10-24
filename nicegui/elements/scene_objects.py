import math
from typing import List, Optional

from .scene_object3d import Object3D


class Group(Object3D):
    def __init__(self) -> None:
        """Group

        This element is based on Three.js' [Group ](https://threejs.org/docs/index.html#api/en/objects/Group) object.
        It is used to group objects together.
        """
        super().__init__("group")


class Box(Object3D):
    def __init__(
        self,
        width: float = 1.0,
        height: float = 1.0,
        depth: float = 1.0,
        wireframe: bool = False,
    ) -> None:
        """Box

        This element is based on Three.js' [BoxGeometry ](https://threejs.org/docs/index.html#api/en/geometries/BoxGeometry) object.
        It is used to create a box-shaped mesh.

        - width: width of the box (default: 1.0)
        - height: height of the box (default: 1.0)
        - depth: depth of the box (default: 1.0)
        - wireframe: whether to display the box as a wireframe (default: `False`)
        """
        super().__init__("box", width, height, depth, wireframe)


class Sphere(Object3D):
    def __init__(
        self,
        radius: float = 1.0,
        width_segments: int = 32,
        height_segments: int = 16,
        wireframe: bool = False,
    ) -> None:
        """Sphere

        This element is based on Three.js' [SphereGeometry ](https://threejs.org/docs/index.html#api/en/geometries/SphereGeometry) object.
        It is used to create a sphere-shaped mesh.

        - radius: radius of the sphere (default: 1.0)
        - width_segments: number of horizontal segments (default: 32)
        - height_segments: number of vertical segments (default: 16)
        - wireframe: whether to display the sphere as a wireframe (default: `False`)
        """
        super().__init__("sphere", radius, width_segments, height_segments, wireframe)


class Cylinder(Object3D):
    def __init__(
        self,
        top_radius: float = 1.0,
        bottom_radius: float = 1.0,
        height: float = 1.0,
        radial_segments: int = 8,
        height_segments: int = 1,
        wireframe: bool = False,
    ) -> None:
        """Cylinder

        This element is based on Three.js' [CylinderGeometry ](https://threejs.org/docs/index.html#api/en/geometries/CylinderGeometry) object.
        It is used to create a cylinder-shaped mesh.

        - top_radius: radius of the top (default: 1.0)
        - bottom_radius: radius of the bottom (default: 1.0)
        - height: height of the cylinder (default: 1.0)
        - radial_segments: number of horizontal segments (default: 8)
        - height_segments: number of vertical segments (default: 1)
        - wireframe: whether to display the cylinder as a wireframe (default: `False`)
        """
        super().__init__(
            "cylinder",
            top_radius,
            bottom_radius,
            height,
            radial_segments,
            height_segments,
            wireframe,
        )


class Ring(Object3D):
    def __init__(
        self,
        inner_radius: float = 0.5,
        outer_radius: float = 1.0,
        theta_segments: int = 8,
        phi_segments: int = 1,
        theta_start: float = 0,
        theta_length: float = 2 * math.pi,
        wireframe: bool = False,
    ) -> None:
        """Ring

        This element is based on Three.js' [RingGeometry ](https://threejs.org/docs/index.html#api/en/geometries/RingGeometry) object.
        It is used to create a ring-shaped mesh.

        - inner_radius: inner radius of the ring (default: 0.5)
        - outer_radius: outer radius of the ring (default: 1.0)
        - theta_segments: number of horizontal segments (default: 8, higher means rounder)
        - phi_segments: number of vertical segments (default: 1)
        - theta_start: start angle in radians (default: 0)
        - theta_length: central angle in radians (default: 2π)
        - wireframe: whether to display the ring as a wireframe (default: `False`)
        """
        super().__init__(
            "ring",
            inner_radius,
            outer_radius,
            theta_segments,
            phi_segments,
            theta_start,
            theta_length,
            wireframe,
        )


class QuadraticBezierTube(Object3D):
    def __init__(
        self,
        start: List[float],
        mid: List[float],
        end: List[float],
        tubular_segments: int = 64,
        radius: float = 1.0,
        radial_segments: int = 8,
        closed: bool = False,
        wireframe: bool = False,
    ) -> None:
        """Quadratic Bezier Tube

        This element is based on Three.js' [QuadraticBezierCurve3 ](https://threejs.org/docs/index.html#api/en/extras/curves/QuadraticBezierCurve3) object.
        It is used to create a tube-shaped mesh.

        - start: start point of the curve
        - mid: middle point of the curve
        - end: end point of the curve
        - tubular_segments: number of tubular segments (default: 64)
        - radius: radius of the tube (default: 1.0)
        - radial_segments: number of radial segments (default: 8)
        - closed: whether the tube should be closed (default: `False`)
        - wireframe: whether to display the tube as a wireframe (default: `False`)
        """
        super().__init__(
            "quadratic_bezier_tube",
            start,
            mid,
            end,
            tubular_segments,
            radius,
            radial_segments,
            closed,
            wireframe,
        )


class Extrusion(Object3D):
    def __init__(
        self,
        outline: List[List[float]],
        height: float,
        wireframe: bool = False,
    ) -> None:
        """Extrusion

        This element is based on Three.js' [ExtrudeGeometry ](https://threejs.org/docs/index.html#api/en/geometries/ExtrudeGeometry) object.
        It is used to create a 3D shape by extruding a 2D shape to a given height.

        - outline: list of points defining the outline of the 2D shape
        - height: height of the extrusion
        - wireframe: whether to display the extrusion as a wireframe (default: `False`)
        """
        super().__init__("extrusion", outline, height, wireframe)


class Stl(Object3D):
    def __init__(
        self,
        url: str,
        wireframe: bool = False,
    ) -> None:
        """STL

        This element is used to create a mesh from an STL file.

        - url: URL of the STL file
        - wireframe: whether to display the STL as a wireframe (default: `False`)
        """
        super().__init__("stl", url, wireframe)


class Gltf(Object3D):

    def __init__(self,
                 url: str,
                 ) -> None:
        """GLTF

        This element is used to create a mesh from a glTF file.

        :param url: URL of the glTF file
        """
        super().__init__('gltf', url)


class Line(Object3D):
    def __init__(
        self,
        start: List[float],
        end: List[float],
    ) -> None:
        """Line

        This element is based on Three.js' [Line ](https://threejs.org/docs/index.html#api/en/objects/Line) object.
        It is used to create a line segment.

        - start: start point of the line
        - end: end point of the line
        """
        super().__init__("line", start, end)


class Curve(Object3D):
    def __init__(
        self,
        start: List[float],
        control1: List[float],
        control2: List[float],
        end: List[float],
        num_points: int = 20,
    ) -> None:
        """Curve

        This element is based on Three.js' [CubicBezierCurve3 ](https://threejs.org/docs/index.html#api/en/extras/curves/CubicBezierCurve3) object.

        - start: start point of the curve
        - control1: first control point of the curve
        - control2: second control point of the curve
        - end: end point of the curve
        - num_points: number of points to use for the curve (default: 20)
        """
        super().__init__("curve", start, control1, control2, end, num_points)


class Text(Object3D):
    def __init__(
        self,
        text: str,
        style: str = "",
    ) -> None:
        """Text

        This element is used to add 2D text to the scene.
        It can be moved like any other object, but always faces the camera.

        - text: text to display
        - style: CSS style (default: '')
        """
        super().__init__("text", text, style)


class Text3d(Object3D):
    def __init__(
        self,
        text: str,
        style: str = "",
    ) -> None:
        """3D Text

        This element is used to add a 3D text mesh to the scene.
        It can be moved and rotated like any other object.

        - text: text to display
        - style: CSS style (default: '')
        """
        super().__init__("text3d", text, style)


class Texture(Object3D):
    def __init__(
        self,
        url: str,
        coordinates: List[List[Optional[List[float]]]],
    ) -> None:
        """Texture

        This element is used to add a texture to a mesh.

        - url: URL of the texture image
        - coordinates: texture coordinates
        """
        super().__init__("texture", url, coordinates)

    def set_url(self, url: str) -> None:
        """Change the URL of the texture image."""
        self.args[0] = url
        self.scene.run_method("set_texture_url", self.id, url)

    def set_coordinates(self, coordinates: List[List[Optional[List[float]]]]) -> None:
        """Change the texture coordinates."""
        self.args[1] = coordinates
        self.scene.run_method("set_texture_coordinates", self.id, coordinates)


class SpotLight(Object3D):
    def __init__(
        self,
        color: str = "#ffffff",
        intensity: float = 1.0,
        distance: float = 0.0,
        angle: float = math.pi / 3,
        penumbra: float = 0.0,
        decay: float = 1.0,
    ) -> None:
        """Spot Light

        This element is based on Three.js' [SpotLight ](https://threejs.org/docs/index.html#api/en/lights/SpotLight) object.
        It is used to add a spot light to the scene.

        - color: CSS color string (default: '#ffffff')
        - intensity: light intensity (default: 1.0)
        - distance: maximum distance of light (default: 0.0)
        - angle: maximum angle of light (default: π/2)
        - penumbra: penumbra (default: 0.0)
        - decay: decay (default: 2.0)
        """
        super().__init__(
            "spot_light", color, intensity, distance, angle, penumbra, decay
        )


class PointCloud(Object3D):
    def __init__(
        self,
        points: List[List[float]],
        colors: List[List[float]],
        point_size: float = 1.0,
    ) -> None:
        """Point Cloud

        This element is based on Three.js' [Points ](https://threejs.org/docs/index.html#api/en/objects/Points) object.

        - points: list of points
        - colors: list of colors (one per point)
        - point_size: size of the points (default: 1.0)
        """
        super().__init__("point_cloud", points, colors, point_size)
