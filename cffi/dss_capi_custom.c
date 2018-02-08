#include <dss_capi.h>

void decompress_complex_csc_matrix(int32_t nrows, int32_t ncols, int32_t *col_ptrs, int32_t *col_indices, double* complex_vals, double* complex_output)
{
    int32_t col_ptr, col_ptr_next;
    int32_t output_step = nrows * 2;
    double *col_out = complex_output;
    int32_t row, col;
    
    for (col = 0; col < ncols; ++col)
    {
        col_ptr = col_ptrs[col];
        col_ptr_next = col_ptrs[col + 1];
        
        while (col_ptr < col_ptr_next)
        {
            row = col_indices[col_ptr];
            col_out[row * 2] = complex_vals[2 * col_ptr];
            col_out[row * 2 + 1] = complex_vals[2 * col_ptr + 1];
            ++col_ptr;
        }
        
        col_out += output_step;
    }
}

void dss_custom_update_loads(int *idx, double *kw, size_t count)
{
    int i;
    
    for (i = 0; i < count; ++i)
    {
        Loads_Set_idx(idx[i]);
        Loads_Set_kW(kw[i]);
    }
}    

void dss_custom_enable_loads(int *idx, int enabled, size_t count)
{
    int i;
    for (i = 0; i < count; ++i)
    {
        Loads_Set_idx(idx[i]);
        CktElement_Set_Enabled(enabled);
    }
}    

void dss_custom_line_currents(double *line_norm_amps, int *all_line_nodes, double* Ia, double* Ib, double* Ic, double* In)
{
    double* I[4] = {Ia, Ib, Ic, In};
    double *currents = 0;
    double norm_amps;
    int *line_nodes;
    double re, im;
    int n, node;
    
    int32_t idx = Lines_Get_First();
    int32_t resultCount = 0;
    
    while (idx > 0)
    {
        line_nodes = all_line_nodes;
        line_nodes += (idx - 1) * 4;
        
        norm_amps = line_norm_amps[idx - 1];
        
        CktElement_Get_Currents(&currents, &resultCount);
        
        for (n = 0; n < 4; ++n)
        {
            node = line_nodes[n];
            if (node == -1)
            {
                break;
            }
            re = currents[2 * n];
            im = currents[2 * n + 1];
            if (norm_amps)
            {
                I[node - 1][idx - 1] = sqrt(re*re + im*im) / norm_amps;
            }
            else
            {
                I[node - 1][idx - 1] = 0.0;
            }
        }

        idx = Lines_Get_Next();
    }
    if (currents)
    {
        DSS_Dispose_PDouble(&currents);
    }
}    
