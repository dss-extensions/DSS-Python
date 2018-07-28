void decompress_complex_csc_matrix(int32_t nrows, int32_t ncols, int32_t *col_ptrs, int32_t *col_indices, double* complex_vals, double* complex_output);
void dss_custom_update_loads(int *idx, double *kw, size_t count);
void dss_custom_enable_loads(int *idx, int enabled, size_t count);
void dss_custom_line_currents(double *line_norm_amps, int *line_nodes, double* Ia, double* Ib, double* Ic, double* In);
