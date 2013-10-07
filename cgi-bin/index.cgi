#!/bin/sh

echo "content-type: text/html; charset=UTF-8"
echo ""

echo "
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\" />
        <title> My Androos</title>
        <script src="/underscore.js" type="text/javascript" charset="utf-8"></script>
        <link rel="stylesheet" href="/bootstrap.css" type="text/css" media="all" />
        <style type="text/css" media="all">
            div {
                white-space: pre-line;
            }
            #env{
                display:none;
            }
            #lsout{
                display:none;
            }
        </style>
    </head>
    <body>
        <div id="env">$( env )</div>
        <div id="lsout">$(busybox ls -lL $PWD/..$QUERY_STRING)</div>
        <div id="table-f">
        </div>
        <script type="text/html" id="tableTemplate">
            <table class="table table-striped">
                <tr>
                    <th>Type</th>
                    <th>File</th>
                    <th>Size</th>
                </tr>
                <% _.each(fList, function(details){%>
                <tr>
                    <td> <%= fTypeMap [ details[0][0] ]%></td>
                    <td><a href=\"<%= encodeURIComponent( details[8] )%>\"><%= details[8]%></a></td>
                    <td><%= details[4] %></td>
                </tr>
                <% }); %>
            </table>
        </script>
        <script type="text/javascript" charset="utf-8">
            var fTypeMap = {};
            fTypeMap['-'] = 'File';
            fTypeMap['d'] = 'Directory';
            var tblTemplate = document.getElementById('tableTemplate').innerHTML; 
            var lsOut = document.getElementById('lsout').innerHTML;
            var elmTble = document.getElementById('table-f');
            var lines = lsOut.split('\\\n');
            fList = [];
            var tBody = [];
            for( var i=1; i< lines.length; i++ ){
                var line = lines[i];
                var tRow = [];
                var fDetails = line.match(/([^ ]+) +([^ ]+) +([^ ]+) +([^ ]+) +([^ ]+) +([^ ]+) +([^ ]+) +([^ ]+) (.*)/).slice(1);
                fList.push( fDetails );
            };
            elmTble.innerHTML = _.template( tblTemplate, fList );
        </script>
    </body>
</html>
"
