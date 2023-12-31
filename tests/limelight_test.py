# import pytest
#
# from components.limelight import Limelight
# from components.limelight_calcs import calc_camera_angle, calc_distance
#
#
# class MockLimelight(Limelight):
#    @property
#    def vertical_offset(self):
#        return 10.0
#
#
# def test_calc_distance():
#    limelight = MockLimelight()
#    d = calc_distance(3, 2, 8, limelight)
#    assert abs(d - 25.988855) < 1e-4
#
#
# def test_calc_camera_angle():
#    limelight = MockLimelight()
#    a1 = calc_camera_angle(10, 2, 8, limelight)
#    assert abs(a1 - 20.963780) < 1e-4
