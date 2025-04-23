  <div class="col-sm-3 col-6 mb-4">
    <div class="row">
      <div class="col-md-12 text-center">
        <img src="media/speakers/{{ talk['PictureFileName'] }}" alt="{{ talk['FirstName'] }} {{ talk['LastName'] }}" class="img-fluid rounded-circle" style="width: 75%">
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 text-center">
        <div class="pt-2">
          <a class="summit" href="#{{ talk['FirstName'] }}-{{ talk['LastName'] }}-talk">
          <h5 class="mt-4 font-weight-medium mb-1"><b>{{ talk['FirstName'] }} {{ talk['LastName'] }}</b><br>{{ talk['Company'] }}</h5>
          <h6 class="subtitle">{{ talk['Position'] }}</h6>
          </a>
        </div>
      </div>
    </div>
  </div>
