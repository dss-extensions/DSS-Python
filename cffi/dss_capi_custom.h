void dss_custom_update_loads(int *idx, double *kw, size_t count);
void dss_custom_enable_loads(int *idx, int enabled, size_t count);
void dss_custom_line_currents(double *line_norm_amps, int *line_nodes, double* Ia, double* Ib, double* Ic, double* In);

extern "Python" int32_t dss_python_cb_plot(void *ctx, char* params);
extern "Python" int32_t dss_python_cb_write(void *ctx, char* messageStr, int32_t messageType);

