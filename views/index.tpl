<head>
        <title>Bekkur</title>
        <link type="text/css" href="/static/style.css" rel="stylesheet">
</head>
<body>
	<h2>Bekkurinn:</h2>
	<table>
	  <tbody><tr>
	    <th>Kennitala</th>
	    <th>Nafn</th>
	    <th>Braut</th>
	  </tr>
      % for nemandi in bekkur['nemendur']:
                <tr>
                        <td>
                                <a href="/nemandi/{{nemandi['kt']}}">{{nemandi['kt']}}</a>
                        </td>
                        <td>{{nemandi['nafn']}}</td>
                        <td>{{nemandi['braut']}}</td>
	            </tr>
      % end

	</tbody></table>


</body>