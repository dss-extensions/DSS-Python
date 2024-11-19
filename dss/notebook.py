from .IDSS import IDSS

try:
    from IPython import get_ipython
    from IPython.display import FileLink, display, display_html, HTML
    from IPython.core.magic import register_cell_magic
    ipython = get_ipython()
    if ipython is None:
        raise ImportError

    import html

    def link_file(fn):
        relfn = os.path.relpath(fn, os.getcwd())
        if relfn.startswith('..'):
            # cannot show in the notebook :(
            display(HTML(f'<p><b>File output</b> ("{html.escape(relfn)}") outside current workspace.<p>'))
        else:    
            display(FileLink(relfn, result_html_prefix=f'<b>File output</b> ("{html.escape(fn)}"):&nbsp;'))

    def show(text):
        display(text)


    @register_cell_magic
    def dss(line, cell):
        if isinstance(DSSPlotCtx, IDSS) and not DSSPlotCtx._api_util._is_oddie:
            DSSPlotCtx.Text.Commands(cell)
        else:
            for line in cell.split('\n'):
                DSSPlotCtx(line)
                res = DSSPlotCtx.Text.Result
                if res.endswith('.DSV'):
                    if _enabled and FilePath(res).exists():
                        plot_dsv(res)

    DSSPlotCtx.AllowChangeDir = False
except:
    def link_file(fn):
        print(f'Output file: "{fn}"')

    def show(text):
        print(text)


    #FileLink('path_to_file/filename.extension')

# import os
# import html
# import tqdm
# from tqdm.notebook import tqdm
# import IPython.display


# dss_progress_bar = None
# dss_progress_desc = ''


@api_util.ffi.def_extern()
def dss_python_cb_write(ctx, message_str, message_type: int, message_size: int, message_subtype: int):
    global dss_progress_bar
    global dss_progress_desc

    # DSS = _ctx2dss(ctx)
    
    message_str = api_util.ffi.string(message_str).decode(api_util.codec)
    if message_type == api_util.lib.DSSMessageType_Error:
        #print('DSS Error:', message_str, file=sys.stderr)
        pass
    elif message_type in (api_util.lib.DSSMessageType_ProgressCaption, api_util.lib.DSSMessageType_ProgressFormCaption):
        #dss_progress_desc = message_str
        # print('Progress Caption:', message_str, file=sys.stderr)
        pass
    elif message_type == api_util.lib.DSSMessageType_Progress:
        #print('DSS Progress:', message_str, file=sys.stderr)
        pass
    elif message_type == api_util.lib.DSSMessageType_FireOffEditor:
        link_file(message_str)
        # try:
        #     # print('DSSMessageType_FireOffEditor')
        #     with open(message_str, 'r') as f:
        #         text = f.read()
            
        #     IPython.display.display({'text/plain': text}, raw=True)
        # except:
        #     print(f'Could not display file "{message_str}"')
        #     return 1

    elif message_type == api_util.lib.DSSMessageType_ProgressPercent:
        try:
            pass
            # n = int(message_str)
            # desc = ''
            # if n == 0 and dss_progress_bar is not None:
            #     dss_progress_bar = None
                
            # if dss_progress_bar is None:
            #     dss_progress_bar = tqdm(total=100, desc=dss_progress_desc)
                
            # if n < 0:
            #     del dss_progress_bar
            #     dss_progress_bar = None
            #     return 0
                
                
            # dss_progress_bar.n = n
            # dss_progress_bar.refresh()
#             if n == 100:
#                 dss_progress_bar.close()
        except:
            import traceback
            traceback.print_exc()
            print('DSS Progress:', message_str)

    # else:
    #     # print(message_type)
    #     # print(message_str)
    #     IPython.display.display({'text/plain': message_str}, raw=True)
    else:
        # do nothing for now...
        pass
        
    return 0
