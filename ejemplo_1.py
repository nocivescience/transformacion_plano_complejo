from manim import *
class analisisi2(Scene):
    CONFIG={
        "plane_config":{
            "line_frequency":0.5
        },
        "num_anchors_to_add_per_line":20,
        "complex_homotopy": lambda z,t:z**(2*t),
        "zoom_factor":0.06
    }
    def setup(self):
        ZoomedScene.setup(self)
        self.zoom_in_to_one_plus_half_i()
        self.write_derivative()
    
    def add_title(self):
        title=MathTex("z \\rightarrow z^2").add_background_rectangle(GREY,opacity=0.5).scale(1.5).to_corner(UL)
        self.play(Write(title))
    def zoom_in_to_one_plus_half_i(self):
        z=complex(1,0.5)
        point=self.background.number_to_point(z)
        point_mob=VectorizedPoint(point)
        frame=self.zoomed_camera.frame
        frame.move_to(point)
        tiny_plane=NumberPlane(
            x_radius=2,y_radius=2,color=GREEN,secondary_color=GREEN_B
        ).replace(frame)
        plane=self.get_plane()
        words=Tex("¿Qué logras apreciar?").add_background_rectangle().next_to(self.zoomed_display,LEFT,aligned_edge=UP)
        arrow=Arrow(words.get_bottom(),self.zoomed_display.get_left())
        VGroup(words,arrow).set_color(YELLOW)
        self.play(FadeIn(plane))
        self.activate_zooming(animate=True)
        self.play(Create(tiny_plane))
        self.wait()
        self.add_transformable_mobjects(plane,tiny_plane,point_mob)
        self.add_foreground_mobjects(words,arrow)
        
        self.apply_complex_homotopy(self.complex_homotopy,
        added_anims=[
            Write(words),
            GrowArrow(arrow),
            MaintainPositionRelativeTo(frame,point_mob)
        ])
    def get_plane(self):
        top_plane=NumberPlane(
            y_radius=config['frame_width']/2,
            x_line_frequency=0.1,
            y_line_frequency=0.1
        )
        self.prepare_for_transformation(top_plane)
        bottom_plane=top_plane.copy()
        tiny_tiny_buff=0.001
        top_plane.next_to(ORIGIN,DOWN,buff=tiny_tiny_buff)
        return VGroup(top_plane,bottom_plane)
    def write_derivative(self):
        pass