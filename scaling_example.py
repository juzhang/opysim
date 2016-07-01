"""
Test script for scaling using gias2's osim module.
"""

import os
import opysim

model_path = os.path.join('example_data', 'gait2392_simbody.osim')
model_out_path = os.path.join('example_data', 'gait2392_scaled.osim')
model = opysim.Model(model_path)
state_0 = model._model.initSystem()

#===================#
# scale whole model #
#===================#
model_scales = [
    opysim.Scale([2.0, 2.0, 2.0], 'model_scale_0', 'femur_r'),
    opysim.Scale([2.0, 2.0, 2.0], 'model_scale_1', 'tibia_r'),
]
model.scale(state_0, *model_scales)

#==============#
# scale a body #
#==============#
test_body = 'femur_l'
body = model.bodies[test_body]
body.scale([1.5, 2.0, 2.5], False)
body.scaleInertialProperties([1.5, 2.0, 2.5], False)
body.scaleMass(1.5)

test_body = 'tibia_l'
body = model.bodies[test_body]
body.scale([1.5, 2.0, 2.5], False)
body.scaleInertialProperties([1.5, 2.0, 2.5], False)
body.scaleMass(1.5)

#===============#
# scale a joint #
#===============#
test_joint = 'knee_l'
joint = model.joints[test_joint]
joint_scales = [
    opysim.Scale([1.5, 2.0, 2.5], 'knee_l_scale_0', 'femur_l'),
    opysim.Scale([1.5, 2.0, 2.5], 'knee_l_scale_1', 'tibia_l'),
]
joint.scale(*joint_scales)

#================#
# scale a muscle #
#================#
test_muscle = 'vas_med_l'
muscle = model.muscles[test_muscle]
muscle_scales = [
    opysim.Scale([1.5, 2.0, 2.5], 'mus_scale_0', 'femur_l'),
    opysim.Scale([1.5, 2.0, 2.5], 'mus_scale_1', 'tibia_l'),
]
state0 = model._model.initSystem()
muscle.scale(state_0, *muscle_scales)

# save
model.save(model_out_path)

# view
viz = model.view_init_state()
