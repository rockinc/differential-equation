import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

init = [1.0]
t_span = [0.0, 5.0]
delta_t = 0.05
t_eval = np.arange(*t_span, delta_t)

def decay(t, x): return x

def euler_method(function, valuable_start, valuable_end, delta_valuable, init_function_value):
    valuable_vector = np.arange(valuable_start, valuable_end, delta_valuable)
    after_value = 0
    function_value_vector = np.array([init_function_value])
    for i_num, i_value in enumerate(valuable_vector):
        if i_num == 0:
            before_value = init_function_value
        else:
            before_value = after_value
        value_increased = function(i_value, before_value) * delta_valuable
        after_value = before_value + value_increased
        function_value_vector = np.append(function_value_vector, np.array([after_value]))
    method_result = np.stack([valuable_vector, function_value_vector[:-1]], 0)
    return method_result

result = euler_method(decay, 0, 5, 0.01, 1)
sol = solve_ivp(decay, t_span, init, method='RK45', t_eval=t_eval)
plt.plot(result[0], result[1], color='r')
plt.plot(sol.t, sol.y[0, :], color='b')
plt.show()
